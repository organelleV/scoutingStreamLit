import pandas as pd
import streamlit as st

def convert_to_export_url(url):
    return url.replace("edit#gid","export?format=csv&gid")
def download_sheet(url):
    sheet_url = convert_to_export_url(url)
    df = pd.read_csv(sheet_url)
    df.to_csv('prematch_download.csv')

sheet_url_input = st.text_input("Google Sheet URL:")
download_sheet(sheet_url_input)
df = pd.read_csv('prematch_download.csv', index_col="Team") # use Prematch Data.csv

matchn_input = st.text_input("Input Match #: ")
matchn = int(matchn_input)

teams = [st.text_input("Enter Team # Red1 (In order of 3 red, 3 blue): "), st.text_input("Enter Team # Red2: "), st.text_input("Enter Team # Red3: "),
         st.text_input("Enter Team # Blue1: "), st.text_input("Enter Team # Blue2: "), st.text_input("Enter Team # Blue3: ")]

st.write("*Match Number:* " + str(matchn) + "")

for num, tn in enumerate(teams):
    if num <= 2:
        st.write(":red_circle:*" + tn + "*:red_circle:")
    else:
        st.write(":large_blue_circle:*" + tn + "*:large_blue_circle:")

    x = df.loc[int(tn)]

    # Auto
    st.write("Auto: ", end="")
    als = ["Low", "Mid", "High"]
    c = 3
    try:
        for i in als:
            if int(x[f"Normal # of Pieces {i} Auto"]) != 0:
                st.write(str(x[f"Normal # of Pieces {i} Auto"]) + f" {i}", end="")
                c -= 1
        if c == 3:
            st.write("No pieces in Auto", end="")
    except ValueError:
        st.write("NaN, ", end="")

    try:
        if float(x["AUTO % Engage"].replace("%", "")) > 50:
            st.write(" and Engage", end="")
        if float(x["AUTO % Mobility"].replace("%", "")) > 50:
            st.write(" and Mobility ", end="")
    except ValueError:
        st.write(", NaN", end="")

    #drivebase
    st.write("Drivebase: " + x["Drive Base"], end="")

    # node
    # dict = {
    #     "Low": float(str(x["% Low Score"]).replace("%", "")),
    #     "Mid": float(str(x["% Mid Score"]).replace("%", "")),
    #     "High": float(str(x["% High Score"]).replace("%", ""))
    # }
    # y = max(float(str(x["% Low Score"]).replace("%", "")), float(str(x["% Mid Score"]).replace("%", "")), float(str(x["% High Score"]).replace("%", "")))
    # for i in dict.values():
    #     if str(i) != "0.0" and (str(i) == "50.0" or str(i) == "33.3"):
    #         st.write("\nNode(s): " + ", ".join([k for k, v in dict.items() if v == i]), end="")
    #         break
    #     else:
    #         st.write("\nNode(s): " + list(dict.keys())[list(dict.values()).index(float(y))] + " Node", end="")
    #         break

    # teleop
    try:
        st.write("Avg Points Scored Teleop: " + str(x["Avg Teleop Points"]))
    except ValueError:
        st.write("Teleop Avg: NaN Error")

    # # feeder
    # st.write("Feeder Type(s): ", end="")
    # try:
    #     dict2 = {
    #         "Ground": float(str(x["% Field Pickup"]).replace("%", "")),
    #         "Single": float(str(x["% Slide Pickup"]).replace("%", "")),
    #         "Double": float(str(x["% High Pickup"]).replace("%", ""))
    #     }

    #     feederls = list(dict2.values())
    #     feederls.sort(reverse=True)
    #     for i in feederls:
    #         if str(i) != "0.0" and str(i) == "50.0" or str(i) == "33.3":
    #             st.write(" ".join([k for k, v in dict2.items() if v == i]), end="")
    #             break
    #         elif str(i) != "0.0":
    #             st.write(list(dict2.keys())[list(dict2.values()).index(i)], end=" ")
    #             break
    # except ValueError:
    #     st.write("NaN Error", end="")

    # defense?
    try:
        st.write("Defense: Yes") if float(x["Defense Performance"]) > 5.0 else st.write("Defense: No")
    except ValueError:
        st.write("Defense: NaN Error")

    # newline  /\_/\
    #         ( o.o )
    #          > ^ <
    st.write("\n")