import logging

import httpx
from carbon_txt.plugins import hookimpl

# every plugin needs a name
plugin_name = "carbon_txt_check_online"


@hookimpl
def process_document(document, logs):
    # we send a HEAD request, as we are not trying to download the file.
    # and check the contents - we just want to see that it's reachable
    response = httpx.head(document.url, follow_redirects=True)

    if response.status_code == 200:
        logs.append(f"{plugin_name}: File is online: {document.url}")
        file_online = True
    else:
        logs.append(f"{plugin_name}: File is offline: {document.url}")
        file_online = False

    check_results = {
        "url": document.url,
        "file_online": file_online,
    }

    # because processing a document can result in multiple results being
    # returned we always return a list of results
    results = [check_results]

    return {
        # return the logs so we see the output in response seen by the user
        "logs": logs,
        # return the name of the plugin, so we can tell the output plugins apart
        "plugin_name": plugin_name,
        # return the results of prcoessing the document - in our case a
        # check to see if it's online
        "document_results": results,
    }
