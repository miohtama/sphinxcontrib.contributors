(function($) {

    "use strict";

    // Transparency rendering directives how to map
    // flattened committer data on the client-side template
    var directives = {

        committer: {
            href: function(elem) {
                return this.html_url;
            },

            title: function() {
                return this.login;
            },

            style: function() {
                // Limit Gravatar size
                var imageURL = this.avatar_url + "?size=48";
                return "background-image: url(" + imageURL + ")";
            }


        },

        // Generate centered image using CSS backgroun
        "avatar-img": {
        },

    };

    /**
     * Go through all commits from Github a build a list of committers.
     *
     *  http://stackoverflow.com/a/19200303/315168
     */
    function getAuthors(commits) {
        var authors = [];
        var consumedAuthors = {};

        $.each(commits, function() {
            if(this.author.avatar_url) {
                // Make sure we an image
                if(consumedAuthors[this.author.login]) {
                    // Make sure this author does not appear twice
                    return;
                }

                consumedAuthors[this.author.login] = true;

                authors.push(this.author);
            }
        });

        return authors;
    }

    $(document).ready(function() {
        var committers = $("#committers");
        var url = committers.attr("data-github-commit-api-url");

        // TODO: Caching the results in LocalStorage here
        // would be nice

        if(!url) {
            return;
        }

        $.getJSON(url, function(data) {
            $(".committer-loader").hide();
            var authors = getAuthors(data);
            $('#committers').render(authors, directives);

        });
    });

})(jQuery);