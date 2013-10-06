# This package may contain traces of nuts
"""

"""

import os

from sh import git

# Have file system path -> Github repository URLs cached
_repo_cache = {}


def get_github_commits_api_url(fpath):
    """ Get a Github hosted file URL.

    http://stackoverflow.com/q/13430769/315168

    :return: None if the information cannot be resolved.
    """

    # Find out .git repo
    path = os.path.dirname(os.path.realpath(fpath))


    # Walk up in the path to find .git,
    # or abort on root
    while path and os.path.dirname(path) != path:

        github_info = _repo_cache.get(path, None)

        # This is the git repo root
        # Resolve its Github url and store in cache
        if (github_info is None) and os.path.exists(os.path.join(path, ".git")):

            git_root = path

            # Work around some pesky sh race condition
            # where running command sometimes returns empty lines.
            # We just rerun this in this case.
            remotes = [u""]
            hack = 5
            while remotes == [u""] and hack > 0:
                remotes = git("--git-dir=%s/.git" % path, "remote", "-v").split("\n")
                hack -= 1

            primary = remotes[0]

            # Assumed format
            parts = primary.split()
            assert len(parts) == 3, "Got git remote info %s, assumed 'origin  git://github.com/plone/wicked.git (fetch)' style" % primary
            name, address, fetch_type = parts

            # Git repository, but not a Github repository
            if not (address.startswith("git://github.com") or address.startswith("git@github.com")):
                if "github" in address:
                    print "Unknown github address format: %s" % address
                return None

            repo_path = None
            for possible_prefix in ("git://github.com/", "git@github.com:"):
                if address.startswith(possible_prefix):
                    repo_path = address[len(possible_prefix):]
                    repo_path, ext = os.path.splitext(repo_path)
                    break

            assert repo_path, "Could not determine Github repositry URL from git address %s" % address

            github_base_url = "https://api.github.com/repos/%s/commits?path=" % repo_path

            # Store repository root and corresponding Github URL
            # for solving the files
            github_info = {"url": github_base_url, "root": git_root}
            _repo_cache[path] = github_info

        # Resolved us on Github
        if github_info:

            rel_path = os.path.relpath(os.path.realpath(fpath), github_info["root"])
            return github_info["url"] + rel_path

        # Go up in the directory tree one level
        path = os.path.dirname(path)

    return None


def html_page_context(app, pagename, templatename, context, doctree):
    """ Update the Sphinx context with author information.
    """

    source = github_commit_url = None

    if doctree:
        source = doctree.attributes['source'] # Path to .rst file

    if source:
        github_commit_url = get_github_commits_api_url(source)

    context["github_commit_url"] = github_commit_url


def setup(app):
    """ Sphinx entry point """
    app.connect('html-page-context', html_page_context)
    app.add_javascript("transparency.min.js")
    app.add_javascript("contributors.js")
    app.add_stylesheet("contributors.css ")