# media_bundler/conf/settings.py

"""
These are the default settings for media_bunder.

You can copy, paste, and modify these values into your own settings.py file.
"""
import os

# This flag determines whether to enable bundling or not.  To assist in
# debugging, we recommend keeping files separate during development and bundle
# them during production, so by default we just use settings.DEBUG, but you can
# override that value if you wish.
USE_BUNDLES = False

# This puts your JavaScript at the bottom of your templates instead of the top
# in order to allow the page to load before script execution, as described in
# YUI rule #5:
# http://developer.yahoo.net/blog/archives/2007/07/high_performanc_5.html
DEFER_JAVASCRIPT = True

# This setting enables bundle versioning and cache busting.  This should be a
# file path to a Python module that will be live when the site is deployed.  The
# bundler will write out Python code defining a dictionary mapping bundle names
# to versions.
BUNDLE_VERSION_FILE = None  # Ex: PROJECT_ROOT + "/bundle_versions.py"

# If bundle versioning is enabled, this setting controls how the bundler
# computes the current version.  Possible values are 'sha1', 'md5', and 'mtime'.
# The md5 and sha1 versioners are preferred because they create less false
# versions.
BUNDLE_VERSIONER = 'sha1'
SITE_ROOT = "/home/adrian/shopnation/shopnation-storefront/"
ASSET_ROOT = SITE_ROOT + "web/htdocs/assets/"
MEDIA_ROOT = ASSET_ROOT + "images/"
CSS_ROOT = ASSET_ROOT + "style/"

def get_files(input_dir):
	for root, dirs, files in os.walk(input_dir):
		return tuple(files)

MEDIA_BUNDLES = (
    # This should contain something like:

    #{"type": "javascript",
    # "name": "myapp_scripts",
    # "path": MEDIA_ROOT + "/scripts/",
    # "url": MEDIA_URL + "/scripts/",
    # "minify": True,  # If you want to minify your source.
    # "files": (
    #     "foo.js",
    #     "bar.js",
    #     "baz.js",
    # )},

    #{"type": "css",
    # "name": "myapp_styles",
    # "path": MEDIA_ROOT + "/styles/",
    # "url": MEDIA_URL + "/styles/",
    # "minify": True,  # If you want to minify your source.
    # "files": (
    #     "foo.css",
    #     "bar.css",
    #     "baz.css",
    #     "myapp-sprites.css",  # Include this generated CSS file.
    # )},

    #{"type": "png-sprite",
    # "name": "myapp_sprites",
    # "path": MEDIA_ROOT + "/images/",
    # "url": MEDIA_URL + "/images/",
    # # Where the generated CSS rules go.
    # "css_file": MEDIA_ROOT + "/styles/myapp-sprites.css",
    # "files": (
    #     "foo.png",
    #     "bar.png",
    #     "baz.png",
    # )},

    {"type": "png-sprite",
     "name": "browse_sprites",
     "path": MEDIA_ROOT + "mow/",
     "url": "../images/",
     # Where the generated CSS rules go.
     "css_file": CSS_ROOT + "my-app.css",
     "files": get_files(MEDIA_ROOT + "mow/")
	},
)

PNG_BUNDLER_NAMES = {
	"browse_sprites":
    {
        "bullet.gif":"h1",
        "dash.png":"h2",
        "filter_checkbox.png":"h3",
    }    
}
