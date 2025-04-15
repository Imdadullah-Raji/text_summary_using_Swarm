from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from swarm import Swarm, Agent



with open('data.csv','r') as d:
    reader = d.readlines()

prompt = "\n".join(reader)

client= Swarm()
csv_summarizer = Agent(
    name="csv summarizer",
    instructions="You will get data in a csv format. The first line is header. Describe it in a single paragraph, Prioritize objects, not the time. Report any anomaly or interesting observation."

)  

response = client.run(
    agent= csv_summarizer,
    messages= [{"role":"user", "content":prompt}]
)
report= response.messages[-1]["content"]

doc = SimpleDocTemplate("output.pdf")
styles = getSampleStyleSheet()
story = []
paragraph = Paragraph(report, styles['Normal'])
story.append(paragraph)

doc.build(story)


