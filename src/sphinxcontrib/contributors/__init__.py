# This package may contain traces of nuts
"""

"""

import os
import urlparse

from sh import git


# Have file system path -> Github repository URLs cached
_repo_cache = {}

def construct_github_url(app, view, path):
    return 'https://github.com/{project}/{view}/{branch}/{path}'.format(
        project=app.config.edit_on_github_project,
        view=view,
        branch=app.config.edit_on_github_branch,
        path=path)


def get_github_commits_api_url(fpath):
    """ Get a Github hosted file URL.

    http://stackoverflow.com/q/13430769/315168

    :return: None if the information cannot be resolved.
    """

    # Find out .git repo
    path = os.path.dirname(fpath)

    # Walk up in the path to find .git,
    # or abort on root
    while path and os.path.dirname(path) != path:

        url = _repo_cache.get(path)
        if url:
            return url

        if os.path.exists(os.path.join(path, ".git")):
            remotes = git.remote("-v").split("\n")

            if len(remotes) == 0:
                return None

            primary = remotes[0]

            # Assumed format
            parts = primary.split()
            assert len(parts) == 3, "Got git remote info %s, assumed 'origin  git://github.com/plone/wicked.git (fetch)' style" % primary
            name, address, fetch_type = parts

            # git@github.com:collective/collective.developermanual.git
            parts = address.split(":")
            assert len(parts) == 2, "Got git remote info %s, assumed 'git@github.com:collective/collective.developermanual.git' style" % address

            repo_path = parts[1]
            repo_path, ext = os.path.splitext(path)

            rel_path = os.path.relpath(fpath, path)

            api_url = "https://api.github.com/repos/%s/commits?path=%s" % (repo_path, rel_path)

            _repo_cache[path] = api_url
            print api_url
            return api_url

        path = os.path.dirname(path)

    return None


def html_page_context(app, pagename, templatename, context, doctree):
    """ Update the Sphinx context with author information.
    """

    source = github_url = None

    if doctree:
        source = doctree.attributes['source'] # Path to .rst file

    if source:
        github_url = get_github_commits_api_url(source)
        print github_url

def setup(app):
    app.connect('html-page-context', html_page_context)