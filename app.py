__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from crew import SalesBdProjectCrew


class SalesBdProjectUI:

    # def load_html_template(self):
    #     with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
    #         html_template = file.read()

    #     return html_template

    def generate_company_summary(self, company_name, company_url):
        inputs = {
            "company_name": company_name,
            "company_url": company_url,
        }
        return SalesBdProjectCrew().crew().kickoff(inputs=inputs)

    def company_url_generation_working(self):

        if st.session_state.generating:
            st.session_state.summary = self.generate_company_summary(
                st.session_state.company_name, st.session_state.company_url
            )

        if st.session_state.summary and st.session_state.summary != "":
            with st.container():
                st.write("Company Summary generated successfully!")
                st.write(st.session_state.summary)
                # st.download_button(
                #     label="Download HTML file",
                #     data=st.session_state.newsletter,
                #     file_name="newsletter.html",
                #     mime="text/html",
                # )
            st.session_state.generating = False

    def sidebar(self):
        with st.sidebar:
            st.title("Company Summary Generator")

            st.write(
                """
                This tool takes a company name and url as the input. \n
                And a team of AI Agents tries to generate a summary for the company!
                """
            )

            st.text_input("Company Name", key="company_name", placeholder="Company Name")
            st.text_input("Website", key="company_url", placeholder="Website Url")

            # st.text_area(
            #     "Your personal message (to include at the top of the newsletter)",
            #     key="personal_message",
            #     placeholder="Dear readers, welcome to the newsletter!",
            # )

            if st.button("Generate Company Summary"):
                st.session_state.generating = True
                


    def render(self):
        st.set_page_config(page_title="Company Summary Generation", page_icon="📧")

        if "company_name" not in st.session_state:
            st.session_state.company_name = ""

        if "company_url" not in st.session_state:
            st.session_state.company_url = ""

        if "summary" not in st.session_state:
            st.session_state.summary = ""

        if "generating" not in st.session_state:
            st.session_state.generating = False

        self.sidebar()

        self.company_url_generation_working()



if __name__ == "__main__":
    SalesBdProjectUI().render()