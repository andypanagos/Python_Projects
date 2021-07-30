
import webbrowser

# Create new html file in write mode
f = open('webpage_generator.html', 'w')

# HTML code that will go into "webpage_generator.html"
html_template = """<html>
    <body>
    <h1>Stay tuned for our amazing summer sale!</h1>
    </body>
    </html>
    """


# Writing code into file
f.write(html_template)

# Close the file
f.close()


# Open file in web browser
webbrowser.open_new_tab('webpage_generator.html')
