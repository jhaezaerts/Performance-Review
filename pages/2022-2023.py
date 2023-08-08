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
    st.markdown(':heart: **Bpost Bank**  \n  '
                '_I have made myself an indispensible component in the finals days of Bpost Bank, where I have shaped '
                'and maintained bridges between business (compliance) and technology (BICC)._')
    st.markdown(':heart: **Texpert Track**  \n  '
                ' _This side project idea attempts to uncover untapped and desirable work in the energy sector. I was'
                'allowed to pitch this idea at the ENR leaders meeting. Furthermore, it allowed me to meet various KPMG '
                'energy experts. The idea is currently still an ongoing topic and will be followed up by myself and '
                'non other than Annelies De Corte and Philip Jeandarme._')
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
    st.image('./images/acknowledging_idea.png')
    st.caption('Jorn De Neve acknowledging the Texpert Track idea and engaging a call to action to our energy leadership at KPMG.')

with goal2:
    st.write('')
    st.subheader("_Actively participate in a relevant GTM / brand campaigns to raise my personal brand and promote the firm’s credentials around data and AI._")
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Work with Lighthouse competence leads to develop a succinct, persuasive and innovative message 1 or more proposals in order to convey a strong client-centric value proposition.**')
    st.markdown(':heart: **Xebia**  \n  '
                ' _Katrien Cloetens has guided me through my first proposal exposure in reasonable detail._')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Work with Lighthouse competence leads to develop internal initiatives, establishing my personal brand as a data and AI professional.**')
    st.markdown(':heart: **GenAI Fridays**  \n  '
                '_This initiative followed from a coffee break room chat with Peter Van den Spiegel. We concluded that due to '
                'the rate of progress in the field of Generative AI, we should have weekly ongoing discussions '
                'on the latest developments and what this could mean for KPMG. This led to a series of GenAI Friday sessions, '
                'hosted by myself. This initiative is currently evolving to become a bi-weekly or monthly GenAI newsletter, '
                'where we can reach large audiences and keep people up to date on latest news, internal developments, '
                'what to look out for and much much more!_')
    st.markdown(":heart: **Generative AI demo's**  \n  "
                '_Due to my exposure to generative AI content, I was asked to demonstrate some of its capabilties to our'
                ' KPMG leadership, going all the way up to the MT. Furthermore, I now have a dedicated 5-minute slot '
                'during our monthly Lighthouse family meeting to talk about what is going on in the world of generative AI._')
    st.markdown("""---""")

    # Action 3
    st.markdown('**Action 3: Share at least six articles related to data / AI on LinkedIn, not necessarily authored by KPMG.**')
    st.markdown(':heart: Follow my activity on [LinkedIn](https://www.linkedin.com/in/jorgohaezaerts/)')
    st.markdown("""---""")

    # Action 4
    st.markdown(':exclamation: **Moving to next year** :exclamation:')
    st.markdown('**Action 4: Write a blog post on the topic of AI: The Emergence of Data-Centric AI.**')
    st.markdown(':heart: Take the [MIT Course](https://dcai.csail.mit.edu/) on data-centric AI')
    st.markdown(':heart: Write a blog post, due April 2024.')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Gallery**')
    st.image('./images/autogpt_mt.jpg')
    st.caption('Ignition organized a session with the MT, where I demonstrated state-of-the-art generative AI capabilities (AutoGPT).')
    st.markdown("""---""")
    st.image('./images/genaifriday_fb1.png')
    st.image('./images/genaifriday_fb2.png')
    st.caption('Some positive feedback on the GenAI Friday sessions.')

with goal3:
    st.write('')
    st.subheader('_I will actively participate and contribute to the competence (cluster) that is most closely aligned with my personal interest._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Lighthouse contributions**')
    st.markdown(':heart: Lighthouse Carrousel:  \n  '
                '_I presented the AAML Lighthouse competence to the batch of new joiners from 2022._')
    st.markdown(":heart: AAML support:  \n  "
                "_I took some responsibility over the organizational aspects of the AAML competence._")
    st.markdown(':heart: [NETFLIX REWIND](https://jhaezaerts-netflix-data-analysis-netflix-data-analysis-lvn3mn.streamlitapp.com/)  \n  '
                '_A data analysis web app that uncovers your Netflix viewing behaviour, to be demonstrated during the Lighthouse family meeting._')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Organize small-scale teambuilding events**')
    st.markdown(':heart: Bouldering  \n  '
                '_As an avid climber, I managed to co-organize no less than three teambuilding bouldering events. '
                'One each with our internal lighthouse AAML and DSAD competences, and one with our project team at Bpost Bank._')
    st.markdown("""---""")


with goal4:
    st.write('')
    st.subheader('_I will help foster a feedback culture within my team by seeking and providing constructive, honest and timely feedback to help myself and those around me develop and grow._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Enroll in relevant courses based on feedback by mentors.**')
    st.markdown(':heart: [Azure Developer](https://online.u2u.be/certified/z0k9)')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Actively provide relevant and constructive feedback to others in the organization, of which at least 50% is upward. Measured through 10 pieces of feedback provided.**')
    st.markdown(':heart: Provide at least 3 pieces of upward feedback.\n'
                '- Dirk :heavy_check_mark:\n'
                '- Filip :heavy_check_mark:\n'
                '- Annelies :heavy_check_mark:\n')
    st.markdown(':heart: Provide at least 3 pieces of equal level feedback.\n'
                '- Stijn :heavy_check_mark:\n'
                '- Zoé :heavy_check_mark:\n'
                '- Julien :heavy_check_mark:\n')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Gallery**')
    st.image('./images/feedback_philip.png')
    st.caption('After providing Philip with feedback, he also gave his two cents about his experiences with me.')
    st.markdown("""---""")
    st.image('./images/stijn.png')
    st.caption('Some equal level feedback received related to project work for BNPPF.')
    st.markdown("""---""")

with goal5:
    st.write('')
    st.subheader('_I will take ownership of my development and career, demonstrating learning agility and challenging myself and others to improve._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Present a data-related session in my group at least 2 times a year on data and AI to share my learnings and help others develop in the latest global trends in that space.**')
    st.markdown(':heart: A brief introduction to Explainable AI :heavy_check_mark:')
    st.markdown(':heart: Data-Centric AI :x:')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Lead by example and get certified in at least 5 data-related topics and expand my skill sets in data engineering and data science.**')
    st.markdown(':heart: Azure Data Fundamentals :heavy_check_mark:')
    st.markdown(':heart: Power Platform :x:')
    st.markdown(':heart: Power BI Data Analyst :x:')
    st.markdown(':heart: Azure Data Engineer :x:')
    st.markdown(':heart: Azure Data Scientist :heavy_check_mark:')
    st.markdown("""---""")

    # Action 3
    st.markdown('**Action 3: Provide continued assistance to colleagues who need technical expertise. Measured through feedback.**')
    st.markdown(':heart: I hosted recurring catch-ups with Zoé to support her with technical aspects of her engagement with BNPPF and ensure optimal quality of work.')
    st.markdown("""---""")

    # Action 4
    st.markdown('**Action 4: Sharpen my coding skills by completing 365 Leetcode coding challenges.**')
    st.markdown(':heart: Follow my progress on [LeetCode](https://leetcode.com/user4180b/).')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Gallery**')
    st.image('./images/xai_feedback_julien.png')
    st.image('./images/xai_feedback_stijn.png')
    st.caption('Some feedback I received from people who attended my knowledge sharing session on explainable AI.')
    st.markdown("""---""")
    st.image('./images/zoe.png')
    st.caption('Zoë provided me with feedback on our extensive project handover at BNPPF.')
    st.markdown("""---""")
    st.image('./images/leetcode_status.png')
    st.caption('I may have overshot myself with 365 leetcode challenges, but happy to have completed more than 100!')

with beyond:
    st.write('')
    st.subheader('_Additional feedback_')
    st.markdown("""---""")
    st.image('./images/feedback_Bo.png')
    st.markdown("""---""")
    st.image('./images/feedback_Stijn.png')
    st.markdown("""---""")
    st.image('./images/fb_morgane.png')
    st.caption('Some encouraging random words of kindness from colleagues I have worked with.')
    st.markdown("""---""")
