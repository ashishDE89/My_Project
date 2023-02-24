import json
import requests
import streamlit as st
import http.client
from urllib.request import urlopen, Request
import pandas as pd
import numpy as np
import base64


st.set_page_config(layout="wide")
st.snow()
original_title = '<h1 style="text-align:center;font-family:Blackadder ITC; color:Orange; font-size: 40px;">Hello There!! I Am Ashish Kothapalli</h1>'
name = '<h1 style="text-align:center;font-family:Brush Script MT; color:Blue; font-size:30px;">Welcome To My Profile</h1>'
summary_title = '<p style="text-align:left;font-family:Berlin Sans FB; color:Orange; font-size: 25px;">What`s my career like:</p>'
toolstech = '<p style="text-align:left;font-family:Berlin Sans FB; color:Orange; font-size: 25px;">What I Use:</p>'
experience = '<p style="text-align:left;font-family:Berlin Sans FB; color:Orange; font-size: 25px;">My Work From The Past/Current:</p>'
education = '<p style="text-align:left;font-family:Berlin Sans FB; color:Orange; font-size: 25px;">Want To See What I Studied:</p>'
me = '<p style="text-align:left;font-family:Berlin Sans FB; color:Orange; font-size: 25px;">Know Me</p>'

st.markdown(original_title, unsafe_allow_html=True)
st.markdown(name, unsafe_allow_html=True)

st.markdown(summary_title,unsafe_allow_html=True)
st.markdown(":point_right:	4+ years of overall IT experience working with storage and data analysis tools making use of cloud technologies.\n"
            "\n:point_right:	Proficient in Azure data services including Azure Data Factory, Azure Databricks, Azure SQL Database, Azure Cosmos DB, Azure Blob Storage, and Azure Synapse Analytics\n"
            "\n:point_right:	Experience working with Databricks (notebooks, Delta Lake, pipelines.\n"
            "\n:point_right:    Hands on experience in developing SPARK applications using Spark tools like RDD transformations, Spark core, Spark Streaming and Spark SQL.\n"
            "\n:point_right:    Experience working with python framework (Pandas, NumPy)\n"
            "\n:point_right:	Working knowledge of Amazon’s Elastic Cloud Compute (EC2) infrastructure for computational tasks and Simple Storage Service (S3) as Storage mechanism.\n"
            "\n:point_right:	Setting up and integrating Hadoop ecosystem tools – HBase, Hive, Sqoop etc\n"
            "\n:point_right:	Hands on experience in writing Spark SQL scripting.\n"
            "\n:point_right:	Experience with creating pipelines, SQL querying and Data ingestion on Databricks")

st.markdown(toolstech, unsafe_allow_html=True)
data = {"Tools": ["Databases","Data Visualization Tools","Analytics Tools","Programming Languages","Integration Tools","Big Data Ecosystem","Operating System"],
            "Technologies": ["SQL Server, MySQL, Oracle SQL Server, MongoDB, Cassandra.","Tableau","AWS Glue, AWS Athena, IAM, S3, EC2, GCP BigQuery, Cloud Storage, Databricks","Python, NoSQL, SQL","Git","HDFS, MapReduce, PySpark, Hive","Linux, Windows"]}
df = pd.DataFrame(data)
st.dataframe(df)

st.markdown(experience, unsafe_allow_html=True)
option = st.selectbox('Choose From Here :male-office-worker:',
             ('Select One','Data Engineer --> Feb ‘ 19 – April`22','Jr. Data Analyst --> Oct ‘18 – Jun ’ 20','Technical Analyst --> Feb` 17 – Sep’ 18'))

if option == 'Data Engineer --> Feb ‘ 19 – April`22':
    st.write(
"**Client**: :blue[_TCS, Hyderabad_]\n"
"\nProject: Create data pipeline for ingestion, process, storage and access to meaningful insurance and claims data for various needs of business, from basic reporting to complex analytical problems.\n"

"\n :blue[What I have done:]\n"

"\n :loudspeaker: Developed ETL data pipelines using Spark.\n"
"\n :loudspeaker: Responsible to ingest data from file streams and databases. Process the data with SQL databases, PySpark.\n"
"\n :loudspeaker: Create Pyspark data frames for analysis.\n"
"\n :loudspeaker: Worked on RDD`s and related functions to work on partitioned data.\n"
"\n :loudspeaker: Worked on reading and writing multiple data formats like JSON,ORC,Parquet on HDFS using PySpark.\n"
"\n :loudspeaker: To implement and maintain the ETL (Extraction, Transformation, used to develop the jobs/Cleansing) Process using Data stage.\n"
"\n :loudspeaker: Worked on building pipelines on Databricks to capture streaming data and load it into data warehouse.\n"
"\n :loudspeaker: Worked on NoSQL databases like Cassandra.\n"
"\n :loudspeaker: Performed data analytics on DataLake using Pyspark on databricks platform.\n"
"\n :loudspeaker: Monitor data flow and maintain the data pipeline on Databricks.\n"
"\n :loudspeaker: Perform Analytics on data extracted from different sources in Databricks.\n"

"Environment: Spark, Python, NumPy, Databricks, SQL, Cassandra, Pyspark, Databricks")

elif option == 'Jr. Data Analyst --> Oct ‘18 – Jun ’ 20':
    st.write("**Client**:  :blue[_Alp Consulting, Hyderabad_]\n"
"\n :blue[What I have done:]\n"
"\n :loudspeaker: Used Sqoop to ingest data from relational databases.\n"
"\n :loudspeaker: Provided technical assistance and data support for new incidents - both technical capability and business issues.\n"
"\n :loudspeaker: Performed basic exploratory data analysis with Pandas and analysis using seaborne.\n"
"\n :loudspeaker: Performed data extraction using SQL queries to extract useful data."
"\n :loudspeaker: Performed statistical calculations using Python NumPy library.\n"
"\n :loudspeaker: Knowledge of cloud data storage (Azure Data Factory, Azure Blob Storage, Synapse Analytics, Azure AD, Azure SQL, Databricks\n"
"\n :loudspeaker: Used Jenkins as a CI/CD tool to deploy.\n"
"\n :loudspeaker: Participate in the Agile meetings to discuss the daily progress.\n"
"\n :loudspeaker: Intermediate working knowledge on MS Excel for data analysis.\n"
"\n :loudspeaker: Provided data analysis to either support or oppose proposed system.\n"
"\n :loudspeaker: Responded to queries either in person or over the phone.\n "

"Environment: Sqoop, Jenkins, Python, NumPy, MS Excel, SQL, Pandas, Azure cloud technologies")

elif option == 'Technical Analyst --> Feb` 17 – Sep’ 18':
    st.write("**Client**: :blue[_IBM, Bangalore_]\n",
             "\n :blue[What I have done:]\n"
"\n :loudspeaker: Engage in technical analysis of software problems using problem determination/problem source. identification.\n"
"\n :loudspeaker: Focus on customer satisfaction by managing client relationships and effectively communicating status and action plans.\n"
"\n :loudspeaker: Collaborate across teams. Utilize technical and negotiation skills to work with team members in development, operations, and support to jointly diagnose problems.\n"
"\n :loudspeaker: Worked on Tableau -Business Intelligence and Analytics tools for connecting to data, creating and managing data sources, Filtering, Actions, and types, formatting data, building Views, Maps, Dashboards publishing data etc\n"
"\n :loudspeaker: Take care of queries from the internal employees as the internal IT and resolve them via calls & emails.\n"
"\n :loudspeaker: Have cross meetings with other teams to discuss and put forth possible solutions for recurring issues.\n"
"\n :loudspeaker: Use Service-Now as a CRM ticketing tool to manage, create and retrieve user records.\n"
"\n :loudspeaker: Create an agile environment and techniques to ease the ITIL process.\n"
"\n :loudspeaker: Monitor incidents and problems raised via the support desk software; assess for service level agreement adherence and intervene with appropriate action.\n"
"\n :loudspeaker: Work with support teams onshore and offshore.\n"
"\n :loudspeaker: Personally, manage major and significant incidents and act as an escalation point to ensure timely resolution of incidents within expectations and SLAs.\n"
"\n :loudspeaker: provide request fulfillment and / or allocate incidents to other members of Technical Run Services via a structured escalation path.\n"
"\n :loudspeaker: Take care of escalations directly from the client and give a timely resolution."
"\n :loudspeaker: Handle a team of six and manage day to day tasks.\n"
"\n :loudspeaker: Assign tasks to the team members and ensure on time resolution.\n"
"\n :loudspeaker: Report to the sector lead on the team`s performance and deliver the daily report.\n")


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(jpg_file):
    bin_str = get_base64(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('https://github.com/ashishDE89/My_Project/blob/main/bg.jpg')

st.markdown(education, unsafe_allow_html=True)

if st.button('Click here :open_book:'):
        st.markdown(":blue[$Bachelor's Degree$:] :school_satchel:\n"
                    "\n:green[College:] Sri Bhagwan Mahaveer Jain College\n"
                    "\n:green[Course:] Biotechnology\n"
                    "\n:green[Year Of Completion:] 2010\n"
                    "\n:green[Location:] Bangalore, India")
        st.markdown(":blue[$Master's Degree$:] :school_satchel:\n"
                    "\n:green[College:] St.Aloysius College Of Management And Technology\n"
                    "\n:green[Course:] BioInformatics\n"
                    "\n:green[Year Of Completion:] 2013\n"
                    "\n:green[Location:] Mangalore, India")
        st.markdown(":blue[$Master's Degree$:] :school_satchel:\n"
                    "\n:green[College:] Wright State University\n"
                    "\n:green[Course:] Industrial Engineering\n"
                    "\n:green[Year Of Completion:] 2016\n"
                    "\n:green[Location:] Fairborn, Ohio")

st.markdown(me,unsafe_allow_html=True)
contact, about_me = st.tabs(["Contact Me","About Me"])
with contact:
    st.write(":email: Email: in.data89@gmail.com \n"
             "\n:telephone_receiver: Phone: (971) 570-7413\n"
             "\n:link:LinkedIn:    https://www.linkedin.com/in/ashish-kothapalli-4286ab265/")
with about_me:
    st.write("I am a learning lad in this vast ocean of the data world. Besides office work, I volunteer at the local library"
             "and love to cook, My curiosity about the world makes me adventurous so love hiking and attend social gatherings. "
             "A new found passion towards Pickle Ball pushes me hard to dive deep into learning the tricks of the game"
              "To top it all, I am avid yoga practioner")
