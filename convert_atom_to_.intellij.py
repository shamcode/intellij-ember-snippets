import re
from os import listdir
from os.path import isfile, join, dirname, realpath

try:
    import cson
except Exception:
    print('Install pycson (pip install cson)')


def get_cwd():
    return dirname(realpath(__file__))


def convert_to_xml(description, snippet):
    xml_string = """
    <template name="%(prefix)s" value="%(body)s$END$" description="%(description)s" toReformat="true">
        <context>
            <option name="JAVA_SCRIPT" value="true" />
        </context>
    </template>
    """ % dict(
        prefix=snippet['prefix'],
        body=snippet['body'].replace('"', "'"),
        description=description
    )
    return xml_string.strip()


def save(filename, snippets):
    name_search = re.search("(import\-(.+))\.cson", filename)
    dest_filename = '%s.xml' % name_search.group(1)
    content = "<templateSet group=\"Ember.js import %(name)s\">\n\t%(snippets)s\n</templateSet>" % dict(
        name=name_search.group(2),
        snippets='\n\t'.join(snippets)
    )
    with open(join(get_cwd(), 'resources', 'liveTemplates', dest_filename), 'w') as dest_file:
        dest_file.write(content)


def main():
    snippets_dir_path = join(get_cwd(), 'atom-ember-snippets', 'snippets')
    for filename in listdir(snippets_dir_path):
        snippet_path = join(snippets_dir_path, filename)
        if not isfile(snippet_path):
            # Ignore directories
            continue
        if not filename.startswith('import-'):
            # Process only "import-*.cson" files
            continue

        with open(snippet_path, 'rb') as cson_file:
            conf = cson.load(cson_file)
            snippets = [convert_to_xml(description, snippet) for description, snippet in conf.values()[0].iteritems()]
            save(filename, snippets)


if __name__ == "__main__":
    main()
