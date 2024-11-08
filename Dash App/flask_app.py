from flask import Flask, render_template, Response
import seaborn as sns
import matplotlib.pyplot as plt
import mpgdata
import io

plt.rcParams["figure.figsize"] = (12, 3)
plt.rcParams['xtick.labelsize'] = 6 # Default x-tick label size 
plt.rcParams['ytick.labelsize'] = 6
plt.rcParams['axes.titlesize'] = 8

# Load Data
df = mpgdata.get_data()

# Create App object
app = Flask(__name__)


# Home page view
@app.route("/")
def home() :
    return render_template("index.html")

# View to generate bar chart
@app.route('/bar_chart.png')
def bar_chart():
    fig = plt.figure(figsize = (12, 3))
    sns.barplot(data = df, x = "origin", y = "horsepower", errorbar=None, hue = "origin", palette="Set2")
    plt.title("Bar Chart: Average Horsepower by Origin", loc = "left", pad = 10, color = "darkblue", size = "large")
    plt.xlabel("")
    plt.ylabel("")
    plt.legend(df.origin.unique(), labelcolor = "midnightblue", fontsize = "x-small")
    plt.grid(axis="y", ls = ":")

    output = io.BytesIO()
    fig.savefig(output, format = "png")
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype="image/png")

# View to generate scatter chart
@app.route('/scatter_chart.png')
def scatter_chart():
    fig = plt.figure(figsize = (12, 3))
    _ = sns.scatterplot(data = df, x = "weight", y = "mpg", hue = "origin", palette="Set2")
    plt.title("Scatter Plot: MPG vs. Weight by Origin", loc = "left", pad = 10, color = "darkblue", size = "large")
    plt.xlabel("Weight", color = "slategray", size = "small")
    plt.ylabel("MPG", color = "slategray", size = "small")
    plt.legend(df.origin.unique(), labelcolor = "midnightblue", fontsize = "x-small")
    plt.grid(axis="y", ls = ":")

    output = io.BytesIO()
    fig.savefig(output, format = "png")
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype="image/png")

# View to generate boxplot chart
@app.route('/box_chart.png')
def box_chart():
    fig = plt.figure(figsize = (12, 3))
    _ = sns.boxplot(data = df, y = "mpg", x = "origin", hue = "origin", palette="Set2")
    plt.title("Box Plot: MPG Distribution by Origin", loc = "left", pad = 10, color = "darkblue", size = "large")
    plt.xlabel("", color = "slategray", size = "small")
    plt.ylabel("", color = "slategray", size = "small")
    plt.legend(df.origin.unique(), labelcolor = "midnightblue", fontsize = "x-small")
    plt.grid(axis="y", ls = ":")

    output = io.BytesIO()
    fig.savefig(output, format = "png")
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype="image/png")


# Launch the app
if __name__ == "__main__" :
    app.run()