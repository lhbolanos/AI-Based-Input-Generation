#include <stdio.h>
#include <libxml/parser.h>

void validateXML(const char *xmlFile) {
    xmlDocPtr doc;

    LIBXML_TEST_VERSION

    // Load XML file
    doc = xmlReadFile(xmlFile, NULL, 0);
    if (doc == NULL) {
        fprintf(stderr, "Failed to parse or validate %s as well-formed XML\n", xmlFile);
        return;
    }

    // Document is well-formed
    printf("%s is a valid XML file.\n", xmlFile);

    // Cleanup
    xmlFreeDoc(doc);
    xmlCleanupParser();
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return -1;
    }

    const char *inputFile = argv[1];
    validateXML(inputFile);

    return 0;
}