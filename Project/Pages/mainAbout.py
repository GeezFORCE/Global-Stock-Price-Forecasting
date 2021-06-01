''' mainAbout.py : Information about the project and authors'''


# External Imports
import streamlit as st
import codecs
import streamlit.components.v1 as stc

def mainAbout(about_html,width=700,height=575):

    # Custom HTML
    about_file=codecs.open(about_html,'r')
    page=about_file.read()
    stc.html(page,width=width,height=height,scrolling=False)
    
    # Markdown
    st.write('\n')
    st.markdown('## Github : [![Github](https://img.shields.io/badge/Made_With-Github-black?style=for-the-badge&logo=Github)](https://github.com/GeezFORCE/MainProject)')
    st.write('\n')
    st.markdown('## License : [![Creative Commons](http://ForTheBadge.com/images/badges/cc-0.svg)](https://creativecommons.org/share-your-work/public-domain/cc0/)')
