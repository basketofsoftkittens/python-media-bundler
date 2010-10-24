

if __name__ == "__main__":

    import sys
    import os
    sys.path.append(os.getcwd())
    from conf import bundler_settings
    import bundler
    import versioning
    
    version_file = bundler_settings.BUNDLE_VERSION_FILE
    if version_file:
        vers_str = bundler_settings.BUNDLE_VERSIONER
        versioner = versioning.VERSIONERS[vers_str]()
    else:
        versioner = None
    # We do the image bundles first because they generate CSS that may get
    # bundled by a CssBundle.
    def key(bundle):
        return -int(isinstance(bundle, bundler.PngSpriteBundle))
    bundles = sorted(bundler.get_bundles().itervalues(), key=key)
    for bundle in bundles:
        bundle.make_bundle(versioner)
    if versioner:
        versioning.write_versions(versioner.versions)
