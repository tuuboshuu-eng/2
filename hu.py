from datetime import datetime

import matplotlib.pyplot as plt

import pandas as pd

from matplotlib.patches import Patch

tasks = [

    ("Project Kickoff & Role Allocation", "2026-05-01", "2026-05-02", "All Team"),

    ("Business Context & Strategic Need", "2026-05-02", "2026-05-05", "You-Jyun"),

    ("Business-IT Alignment", "2026-05-04", "2026-05-08", "You-Jyun"),

    ("Schallmo Framework & Scope", "2026-05-06", "2026-05-10", "You-Jyun"),

    ("Integration Review (Strategy)", "2026-05-10", "2026-05-14", "You-Jyun"),

    ("Privacy Planning", "2026-05-05", "2026-05-09", "Yue Liu"),

    ("Cybersecurity Planning", "2026-05-07", "2026-05-12", "Yue Liu"),

    ("Expected Loss & Risk Controls", "2026-05-10", "2026-05-14", "Yue Liu"),

    ("Compliance & Integration Review", "2026-05-13", "2026-05-16", "Yue Liu"),

    ("Target Architecture & WBS", "2026-05-04", "2026-05-08", "Planning Team"),

    ("Agile Delivery & Sprint Roadmap", "2026-05-07", "2026-05-11", "Planning Team"),

    ("Requirements & Stakeholder Management", "2026-05-10", "2026-05-15", "Planning Team"),

    ("Budget, Risk & Quality Planning", "2026-05-12", "2026-05-17", "Planning Team"),

    ("SDLC & Agile Execution Process", "2026-05-10", "2026-05-15", "Execution Team"),

    ("KPI & Monitoring Logic", "2026-05-14", "2026-05-18", "Execution Team"),

    ("Full Report Integration", "2026-05-18", "2026-05-21", "All Team"),

    ("Formatting, References & Final Review", "2026-05-21", "2026-05-24", "All Team"),

    ("Final Submission Preparation", "2026-05-24", "2026-05-25", "All Team"),

]

df = pd.DataFrame(tasks, columns=["Task", "Start", "Finish", "Owner"])

df["Start"] = pd.to_datetime(df["Start"])

df["Finish"] = pd.to_datetime(df["Finish"])

df["Duration"] = (df["Finish"] - df["Start"]).dt.days

owner_colors = {

    "You-Jyun": "#1f77b4",

    "Yue Liu": "#d62728",

    "Planning Team": "#2ca02c",

    "Execution Team": "#9467bd",

    "All Team": "#ff7f0e"

}

fig, ax = plt.subplots(figsize=(18, 10))

for _, row in df.iterrows():

    ax.barh(

        row["Task"],

        row["Duration"],

        left=row["Start"].toordinal(),

        color=owner_colors[row["Owner"]],

        edgecolor='black',

        height=0.6

    )

date_ticks = pd.date_range(start="2026-05-01", end="2026-05-25", freq="2D")

ax.set_xticks([d.toordinal() for d in date_ticks])

ax.set_xticklabels([d.strftime("%d %b") for d in date_ticks], rotation=45, fontsize=11)

ax.set_title(

    "INFS8205 A5 Digital Strategy Team Gantt Chart\nDeadline: 25 May 2026",

    fontsize=20

)

ax.set_xlabel("Date", fontsize=14)

ax.set_ylabel("Tasks", fontsize=14)

legend_elements = [

    Patch(facecolor=color, edgecolor='black', label=owner)

    for owner, color in owner_colors.items()

]

ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

deadline = datetime(2026, 5, 25).toordinal()

ax.axvline(deadline, color='red', linestyle='--', linewidth=2)

ax.text(deadline, -1, "Submission Deadline", color='red', fontsize=11)

plt.tight_layout()

output_path = "/mnt/data/INFS8205_A5_Team_Gantt_Chart.png"

plt.savefig(output_path, dpi=300, bbox_inches='tight')

print(output_path)
