import BaseHTTPServer, os

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # ...page template...
    Page = '''\
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''

    def do_GET(self):
        try:
            # Figure out what exactly is being requested
            full_path = os.getcwd() + self.path

            # it doesn't exist...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            # it's a file
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # it's something we don't handle
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))

        # Handle errors
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)

    Error_Page = """\
<html>
<body>
<h1>Error accessing {path}</h1>
<p>{msg}</p>
</body>
</html>
"""
    
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def create_page(self):
    	values = {
    		'date_time':self.date_time_string(),
    		'client_host':self.client_address[0],
    		'client_port':self.client_adress[0],
    		'command':self.command,
    		'path':self.path
    	}
    	page = self.Page.format(**values)
    	return page


if __name__ == '__main__':
	serverAddress = ('', 8000)
	server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
	server.serve_forever()
	