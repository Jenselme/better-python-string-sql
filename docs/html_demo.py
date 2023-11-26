def main():
    # Basic tests
    print("<p>value</p>")
    # Check rendering.
    print("<p class=\"cls\">Value</p>")
    # Check rendering.
    print("<-- Comment -->")
    # Check rendering.

    # More complete tests
    print("""
    <!--html-->
    <h1>I am a highlighted html</h1>
    hello
    <p class="cls">world</p>
    <!--!html-->
    <!--htmlcomment-->
    <h1>I am also a highlighted html</h1>
    <!--!htmlcomment-->
    <h1>I amd not a highlighted html</h1>
    """)
    # Check rendering.
    print("""
    <table>
    <tr>
        <td>100</td>
    </tr>
    </table>

    <hr>
    <h2>1 Row and 3 Columns:</h2>
    <table>
    <tr>
        <td>100</td>
        <td>200</td>
        <td>300</td>
    </tr>
    </table>
    """)
    # Check rendering.
    print("""
    <table class="cls">
    <tr class="cls"><td class="toto">100</td></tr>
    </table>""")
    # Check rendering.
    print("""
    <table class="cls" id="id">
    <tr class="cls"><td class="toto">100</td></tr>
    </table>""")
    # Check rendering.

    # Check with custom tags.
    print("""<custom-tag>Value</custom-tag>""")
    # Check rendering.
    print("""<custom-tag class="toto">Value</custom-tag>""")
    # Check rendering.

    # Check various termination cases.
    print("""<custom-tag class="toto">Value</custom-tag>""", "value")
    # Check rendering.
    print("""<custom-tag class="toto">Value</custom-tag>""","value")
    # Check rendering.

    # Check placeholder strings that looks like tags but are not closed.
    print(""""<string>""")
    # Check rendering.
    print(""""<string>
""")
    # Check rendering.
    print("""<string class="toto">""")
    # Check rendering.
    print('<string>')
    # Check rendering.
    print('<string class="toto">')
    # Check rendering.
    print("<string class=\"toto\">")
    # Check rendering.
    print("<string class='toto'>")
    # Check rendering.

    # Data before the string, extension shouldn’t start.
    print("""toto <p class="toto">Coucou</p>""")
    # Check rendering.

    # Check rendering.

    # This is not supported.
#    print(arg, """"<string></string
# """, 'eval')
