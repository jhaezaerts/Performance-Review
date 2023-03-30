import streamlit as st

st.title('Performance Review 2023')
st.title('')
goal1, goal2, goal3, goal4, goal5, beyond = st.tabs(['Goal 1', 'Goal 2', 'Goal 3', 'Goal 4', 'Goal 5', 'Beyond My Goals'])

with goal1:
    st.write('')
    st.subheader('_With passion and purpose, I will collaborate closely with clients to co-create innovative approaches and leading edge solutions._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Provide best practice solutions and demonstrate KPMG’s differentiation for clients.**')
    st.markdown(':heart: Bpost Bank: _To the best of my abilities, I hand in deliverables with the end user in mind and with meticulous attention to detail._')
    st.markdown(':heart: Texpert Track: _This side project idea will attempt to uncover untapped and desirable work in the energy sector. '
                'The work would ideally be a steep learning curve for a data engineering profile. More on this soon._')
    st.markdown("""---""")

    # Action 2
    st.markdown("**Action 2: Ensure effective direction and monitoring is in place to maximize the benefits from the engagement.**")
    st.markdown(':heart: _I am fully staffed on Bpost Bank in 2023. My goal would be that there is no backlog for resources in Compliance and BI as they are migrating to BNPPF. '
                'In that way, all resources can be optimally deployed by BNPPF after the migration._')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Gallery**')
    st.image('./images/BPB_extension_BICC.png')
    st.caption('At Bpost Bank, they were eager to have my contract extended.')
    st.markdown("""---""")
    st.image('./images/feedback_Morgane_1.PNG')
    st.image('./images/feedback_Morgane_2.PNG')
    st.caption('Quite pleasant mid-year feedback I have received from my team lead at Bpost Bank (17/20).')
    st.markdown("""---""")

with goal2:
    st.write('')
    st.subheader("_Actively participate in a relevant GTM / brand campaigns to raise my personal brand and promote the firm’s credentials around data and AI._")
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Work with Lighthouse competence leads to develop a succinct, persuasive and innovative message in 2 proposals or pitches in order to convey a strong client-centric value proposition.**')
    st.markdown(':heart: Xebia: _Katrien has guided me through my first proposal exposure in reasonable detail._')
    st.markdown(':heart: TBD')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Share at least six articles related to data / AI on LinkedIn, not necessarily authored by KPMG.**')
    st.markdown(':heart: Follow my activity on [LinkedIn](https://www.linkedin.com/in/jorgohaezaerts/)')
    st.markdown("""---""")

    # Action 3
    st.markdown('**Action 3: Write a blog post on the topic of AI: The Emergence of Data-Centric AI.**')
    st.markdown(':heart: Take the [MIT Course](https://dcai.csail.mit.edu/) on data-centric AI')
    st.markdown(':heart: Share knowledge on this topic.')
    st.markdown(':heart: Write a blog post.')

with goal3:
    st.write('')
    st.subheader('_I will actively participate and contribute to the competence (cluster) that is most closely aligned with my personal interest._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Lighthouse contributions**')
    st.markdown(':heart: Lighthouse Carousel: _I presented the AAML subcompetence to the batch of new joiners from 2022._')
    st.markdown(":heart: AAML support: I took some responsibility over the organizational aspects of the AAML competence.\n"
                "- _I sent out a poll to the team members to establish who wants to remain part of the core team._\n"
                "- _The AAML Teams channel has been updated to allow for improved file sharing, task management and holiday planning._\n"
                "- _I've built a basic setup of the AAML confluence page on KPMG Source which could be finetuned when/if the need should arise._\n"
                "- _I proposed to set up a bi-weekly core team meeting instead of monthly to ensure better alignment within the team._\n"
                "- _I took the liberty of revamping the core team meeting slides._\n"
                "- _Last but not least, I try to provide optimal general support to the AAML competence lead in terms of completing typical, tedious (junior) tasks to the best of my abilities. 'It's a dirty job, but someones gotta do it.'_")
    st.markdown(':heart: [BART](https://generative-ai-consulting.streamlit.app/) _: a generative AI POC using OpenAI services ChatGPT and Whisper._')
    st.markdown(':heart: [NETFLIX REWIND](https://jhaezaerts-netflix-data-analysis-netflix-data-analysis-lvn3mn.streamlitapp.com/) _: a data analysis web app that uncovers your Netflix viewing behaviour._')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Organize small-scale team building events**')
    st.markdown(':heart: Meet with Sarah Michels to discuss location, timing, budget, type of activities, etc.')
    st.markdown("""---""")


with goal4:
    st.write('')
    st.subheader('_I will help foster a feedback culture within my team by seeking and providing constructive, honest and timely feedback to help myself and those around me develop and grow._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Enroll in relevant courses based on feedback by mentors.**')
    st.markdown(':heart: leadership course - BVR')
    st.markdown(':heart: Azure Developer - KC')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Actively provide relevant and constructive feedback to others in the organization, of which at least 50% is upward. Measured through 10 pieces of feedback provided.**')
    st.markdown(':heart: Provide 5 pieces of upward feedback.\n'
                '- Dirk :heavy_check_mark:\n'
                '- Filip :heavy_check_mark:\n'
                '- Bart\n'
                '- TBD\n'
                '- TBD\n')
    st.markdown(':heart: Provide 5 pieces of equal level feedback.\n'
                '- Stijn :heavy_check_mark:\n'
                '- Zoé\n'
                '- Julien\n'
                '- Yasser\n'
                '- TBD\n')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Gallery**')
    st.image('./images/feedback_philip.png')
    st.caption('After providing Philip with feedback, he also gave his two cents about his experiences with me.')
    st.markdown("""---""")

with goal5:
    st.write('')
    st.subheader('_I will take ownership of my development and career, demonstrating learning agility and challenging myself and others to improve._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Present a data-related session in my group at least 2 times a year on data and AI to share my learnings and help others develop in the latest global trends in that space. (1) Netflix Wrapped Up (2) AI Advancements and Lookahead**')
    st.markdown(':heart: A brief introduction to Explainable AI :heavy_check_mark:')
    st.markdown(':heart: Data-Centric AI')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Lead by example and get certified in at least 5 data-related topics and expand my skill sets in data engineering and data science.**')
    st.markdown(':heart: Azure Data Fundamentals :heavy_check_mark:')
    st.markdown(':heart: Power Platform')
    st.markdown(':heart: Power BI Data Analyst')
    st.markdown(':heart: Azure Data Engineer')
    st.markdown(':heart: Azure Data Scientist :heavy_check_mark:')
    st.markdown(':heart: Azure Developer ')
    st.markdown(':heart: Azure Administrator')
    st.markdown(':heart: Azure Devops')
    st.markdown(':heart: Azure Solutions Architect')
    st.markdown(':heart: ML Course - UGent - BVR')
    st.markdown("""---""")

    # Action 3
    st.markdown('**Action 3: Provide continued assistance to colleagues who need technical expertise. Measured through feedback.**')
    st.markdown(':heart: I attend recurring catch-ups with Zoé to support her with technical aspects of her engagement with BNPPF and ensure optimal quality of work.')
    st.markdown("""---""")

    # Action 4
    st.markdown('**Action 4: Contribute to the texpert track by offering myself as a texpert and developing a side project that brings value to the firm.**')
    st.markdown(':heart: My side project idea is currently under development.')
    st.markdown("""---""")

    # Action 5
    st.markdown('**Action 5: Sharpen my coding skills by completing 365 Leetcode coding challenges.**')
    st.markdown(':heart: Follow my progress on [LeetCode](https://leetcode.com/user4180b/).')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Gallery**')
    st.image('./images/xai_feedback_julien.png')
    st.image('./images/xai_feedback_stijn.png')
    st.caption('Some feedback I received from people who attended my knowledge sharing session on explainable AI.')
    st.markdown("""---""")

with beyond:
    st.write('')
    st.subheader('_Additional feedback_')
    st.markdown("""---""")
    st.image('./images/feedback_Bo.png')
    st.image('./images/feedback_Stijn.png')
    st.caption('Some encouraging random words of kindness from colleagues I have worked with.')
    st.markdown("""---""")

