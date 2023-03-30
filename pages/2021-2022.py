import streamlit as st

st.title('Performance Review 2022')
st.title('')
goal1, goal2, goal3, goal4, beyond = st.tabs(['Goal 1', 'Goal 2', 'Goal 3', 'Goal 4', 'Beyond My Goals'])

with goal1:
    st.write('')
    st.subheader('_I will actively participate and contribute to the competence cluster that is most closely aligned with my personal interest._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Present a technical session in my group at least 1 time in the coming year in the area of artificial intelligence, sharing my learnings and help others develop in the latest global trends in that space.**')
    st.markdown(':heart: Mid-September, I will present a session on the Microsoft Responsible AI Dashboard during the AAML Knowledge Sharing Session.')
    st.markdown(':heart: I will give the introductory presentation of the AAML Competence during the onboarding week of the new Junior Advisors from 2022.')
    st.markdown(':heart: End of September, I will post a technical blog for AAML marketing purposes which will be shared to the public.')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Lead by example and dedicate 5-8 hours per month dedicated to learning and expanding my skillset in programming, data and AI.**')
    st.markdown(':heart: I attended **Dataminds Connect 2021** with Lighthouse Legends Jan Verdickt, Kristof De Middelaere, Jeroen Bolle and Viktor Van Beersel.')
    st.markdown(':heart: I took part in **Google Hash Code 2022** in a team with Robin Bracke and Joris Renkens.')
    st.markdown(':heart: I attended the **Responsible AI Conference 2022** at the Microsoft office in Zaventem.')
    st.markdown(':heart: I completed the Machine Learning Specialization course on Coursera. A world-renowned ML beginners course taught by Andrew Ng.  Check out my [certificate](https://www.coursera.org/account/accomplishments/specialization/certificate/DXMA8S6VVEMW).')
    st.markdown(':heart: I completed 8 [LeetCode](https://leetcode.com/user4180b/) programming challenges.')
    st.markdown(':heart: I created a web app called [Netflix Rewind](https://jhaezaerts-netflix-data-analysis-netflix-data-analysis-lvn3mn.streamlitapp.com/) in Python and shared it with the Lighthouse family.')
    st.markdown("""---""")

    # Action 3
    st.markdown('**Action 3: Develop and propose one gamified, educational idea to our technical colleagues within KPMG Lighthouse, such that their relevant skills are brushed up, improved and actively used.**')
    st.markdown(':heart: This action was put into effect by Joris Renkens, where he would offer weekly coding challenges to people who want to stay more in tune with their programming skills.')
    st.markdown('Offer:')
    st.markdown('_→ Programming challenges to be solved in a programming language of choice_')
    st.markdown('_→ Communication through Microsoft Teams - Lighthouse Family_')
    st.markdown('_→ Three new challenges every week (easy, intermediate, hard)_')
    st.markdown('_→ Leaderboard on Excel_')
    st.markdown('Conclusion: People did not have enough time nor interest for us to further expand on the idea.')
    st.markdown("""---""")

    # Gallery
    st.markdown('**Action Gallery**')
    st.image('./images/AAML_core_team_no_border.png')
    st.caption('Proud member of the Advanced Analytics and Machine Learning Competence')
    st.markdown("""---""")
    st.image('./images/lighthouser_of_the_month.png')
    st.caption('I became Lighthouser of the Month, together with Wout Slaets, for our contribution to a Lighthouse HR event in Leuven.')
    st.markdown("""---""")
    st.image('./images/python_challenges.png')
    st.caption('The weekly coding challenge.')
    st.markdown("""---""")
    st.image('./images/netflix_webapp.png')
    st.caption('Sharing my web app idea to the Lighthouse Family Teams chat.')
    st.markdown("""---""")
    st.image('./images/skitrip.jpg')
    st.caption('I went on the annual KPMG ski-trip, embodying the One Advisory team spirit.')
    st.markdown("""---""")
    st.image('./images/dataminds_2021_stand.jpg')
    st.caption('Jeroen Bolle proudly manning our KPMG stand at Dataminds Connect 2021.')
    st.markdown("""---""")
    st.image('./images/dataminds_2021_darts.jpg')
    st.caption('Jeroen Bolle in the process of winning a brand new darts set.')
    st.markdown("""---""")
    st.image('./images/dataminds_2021_JV.jpg')
    st.caption("Jan Verdickt at Arinti's stand during DataMinds Connect 2021. As always, working hard. ...Or hardly working?")
    st.markdown("""---""")
    st.image('./images/google_hash_2022_robin.jpg')
    st.caption('Robin during the Google Hash Code. Our nights filled with coding and our bellies filled with pizza.')
    st.markdown("""---""")
    st.image('./images/responsible_ai_conference_2022.jpg')
    st.caption('Front row at the Responsible AI Conference, organised by Arinti and Microsoft.')
    st.markdown("""---""")
    st.image('./images/paintball.jpg')
    st.caption('The annual Lighthouse social event, which was a paintball session followed by a delicious barbecue in the evening.')
    st.markdown("""---""")
    st.image('./images/triathlon.png')
    st.caption('Taking our physical abilities to the limit during the annual KPMG triathlon event.')
    st.markdown("""---""")
    st.image('./images/ccs.png')
    st.caption('Our final meeting at the intensive four-day, resident Core Consulting Skills course in Grimbergen.')


with goal2:
    st.write('')
    st.subheader('_I will start to develop an external network and build knowledge of industry, market trends, competitor activity and products/services._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Organize monthly meetings with my superiors at BNP to talk about short-term and long-term goals and how they relate to the big picture at BNPPF.**')
    st.markdown(':heart: Bi-weekly, we start the day with a stand-up meetings over coffee, discussing both business, pleasure and life. Secondly, I’m part of the CMCC data community that organizes weekly meetings, where we do a tour-de-table and discuss important topics (issues, changes, innovation). Lastly, I have organized a weekly status update meeting on a specific project for which I am responsible (data side).')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Regularly perform sector-specific data analytics assignments, ensuring thorough understanding of the task at hand and its global context.**')
    st.markdown(':heart: 20% - 50% of my time with BNP consists of ad hoc analysis requests. As I grew more knowledgeable about the business and the tools, so did the quality of my analyses.')


with goal3:
    st.write('')
    st.subheader('_With passion and purpose, I will work with BNP Paribas Fortis to co-create innovative approaches and leading edge solutions._')
    st.markdown("""---""")

    # Action 1
    st.markdown('**Action 1: Be a key contributor to the Cash Management Competence Center Data Analytics Team, providing best practice solutions and demonstrating KPMG’s differentiation for data-related engagements.**')
    st.markdown('I carried out two ideas that achieved a community-wide impact.')
    st.markdown('**:heart: Dashboard Alerting**')
    st.markdown('_Context:_ The dashboard I am responsible for running is but a link in the chain. This initial dashboard signifies that raw data has been cleaned and can be further processed or visualized.')
    st.markdown('_Problem:_ Initially, I manually had to notify 1 or 2 people by mail when my dashboard had been refreshed. They would then go on to notify other people. Sometimes it happened that one forgot to send a mail and in that case, people were not up to date with the latest data.')
    st.markdown('_Solution:_ Tableau has a functionality that allows automated alerting to a specified group of people at each dashboard refresh with new data.')
    st.markdown('_Impact:_ Eight key stakeholders in the community are immediately up-to-date with the latest data refresh and can perform their tasks in the subsequent chain of activities without any delay. This idea was briefly mentioned by Joris Renkens in one of the LHFM.')
    st.markdown('**:heart: Outlook Automation Script using Python**')
    st.markdown('_Context:_ We receive raw data in three ways. By mail, through SharePoint or data is immediately dropped in the datalake.')
    st.markdown('_Problem:_ On average, 25 mails come in every day, each of which contain an attachment with raw data that needs to be manually saved to the datalake. This is a significant manual burden, especially if this is not kept up with, e.g. after a weekend or a long vacation. (4 days out of office means manually saving attachments of 100 different emails!)')
    st.markdown('_Solution:_ I wrote a Python automation script that is able to communicate with Outlook and automatically save all raw data to specified destinations.')
    st.markdown('_Impact:_ The manual burden has been reduced to one click per day. This was initially only developed for my immediate manager, but due to its success and ease of use, this topic has been presented at our weekly community meeting (16 participants) and now the automation script is being used across the community.')
    st.markdown("""---""")

    # Action 2
    st.markdown('**Action 2: Eliminate over 50% of all unnecessary manual interventions by the end of the engagement term, in order to achieve high efficiency gains and transform the job position such that its successor can focus on the core business.**')
    st.markdown(':heart: Project 1: Payments & Collections')
    st.markdown("_Efficiency gains:_ 10 out of 12 data pipelines for which I am responsible in this context have been automated. My manager's workload has also been slightly alleviated by automating some of his data pipelines. Between one and two hours per week saved.")
    st.markdown(':heart: Project 2: Pn Country Monitoring')
    st.markdown('_Efficiency gains:_ Complete overhaul. Rebuilt the data pipelines from the ground up with the aim of better understanding, higher accuracy, more documentation, functionalities and automated processes. Improvement as opposed to the old pipelines have not (yet) been quantified.')
    st.markdown(':heart: Project 3: FX Reports')
    st.markdown('_Efficiency gains:_ Complete overhaul. The data pipeline I inherited produced false and incomplete data. Ever since the new pipeline has been in production, no errors have been discovered. Went from +- 2 complaints per month to 0 complaints per month.')
    st.markdown(':heart: Project 4: Regulatory Reporting: XML Generator')
    st.markdown('_Efficiency gains:_ Not aware of the previous process, but a CSV to XML conversion script was written in Python that runs in mere seconds.')
    st.markdown("""---""")

    # Action 3
    st.markdown('**Action 3: Present dashboards available to specific stakeholders such that the frequent stream of ad hoc requests are reduced by 30%.**')
    st.markdown(':heart: Our community took the initiative to provide training to client-facing employees within BNPPF with the goal of teaching how they can perform analyses on our range of Tableau Dashboards. This should enable all users to generate figures and reports without the need for an intermediary data analyst. I co-hosted the training and performed after-service.')
    st.markdown("""---""")


with goal4:
    st.write('')
    st.subheader('_I will build on professional qualification by undertaking relevant functional or sector-specific training._')
    st.markdown("""---""")

    # Action
    st.markdown('**Within the timespan of one year, professional certifications will be attained for the following**')
    st.markdown(':heart: Alteryx Designer Core – _A data analysis / data engineering tool currently used at BNP Paribas Fortis._')
    st.markdown('Check out my [certificate](https://www.credly.com/badges/88f026e6-9918-4425-aed5-885744b6e8d2?source=linked_in_profile)!')
    st.write('')
    st.markdown(':heart: Microsoft Azure Fundamentals – _Basic cloud computing concepts in Azure_')
    st.markdown('Check out my [certificate](https://www.credly.com/badges/89f5f127-7868-4388-ada4-08a846d65b7b/linked_in_profile)!')
    st.write('')
    st.markdown(':heart: Microsoft Azure Fundamentals – _Basic AI and machine learning concepts in Azure_')
    st.markdown('Check out my [certificate](https://www.credly.com/badges/611d1375-bbe7-4376-8f2e-9ca2545c2439/linked_in_profile)!')
    st.write('')
    st.markdown(':heart: The Microsoft Data Scientist Associate – _Advanced Data Scientist toolbox in Azure_')
    st.markdown('Expected completion: September 2022')

with beyond:
    st.write('')
    st.subheader('_Additional feedback_')
    st.markdown("""---""")
    st.image('./images/feedback_cedric.png')
    st.caption('Feedback from Cédric Therasse regarding project ADV_TECH_LH_BIA BNPPF - CMCC ANALYTICS SUPPORT 102021')
    st.markdown("""---""")
    st.image('./images/feedback_ccs_annelies.png')
    st.caption('Feedback from Annelies Decorte regarding the CCS training.')
    st.markdown("""---""")
    st.image('./images/feedback_joris.png')
    st.caption('Mid-year feedback from Joris Renkens.')
    st.markdown("""---""")
    st.image('./images/feedback_colruyt_joris.png')
    st.caption('Feedback from Joris Renkens regarding my contribution to a project with Colruyt.')
    st.markdown("""---""")
    st.image('./images/feedback_benny_bogaerts.png')
    st.caption('Got a shout out from Benny Bogaerts during the Monthly Technology Knowledge Sharing Session for my work with the KPMG Markets committee.')
