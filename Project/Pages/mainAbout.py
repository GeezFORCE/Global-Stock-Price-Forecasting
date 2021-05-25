''' mainAbout.py : Information about the project and authors'''


# External Imports
import streamlit as st
import codecs
import streamlit.components.v1 as stc

def mainAbout(about_html,width=700,height=575):
    about_file=codecs.open(about_html,'r')
    page=about_file.read()
    stc.html(page,width=width,height=height,scrolling=False)
    

    st.write('\n')
    st.markdown('## Gitlab : [![Gitlab](https://img.shields.io/badge/Made_With-Gitlab-orange?style=for-the-badge&logo=Gitlab)](https://gitlab.com/GeezFORCE/mainproject)')
    st.write('\n')
    st.markdown('## License : [![Creative Commons](http://ForTheBadge.com/images/badges/cc-0.svg)](https://creativecommons.org/share-your-work/public-domain/cc0/)')
