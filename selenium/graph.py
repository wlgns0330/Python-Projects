import os
import json
import matplotlib.pyplot as plt

def graph(title):
    base_dir = os.path.join("Comment_Analysis", title)
    filepath = os.path.join(base_dir, "data.txt")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        n = len(data["vader"])

        plt.plot(range(1, n + 1), [0]*n, color="black")
        for name in data:
            plt.plot(range(1, n + 1), data[name], label=name)

        plt.xlabel("Episodes")
        plt.ylabel("Polarity")
        plt.title(f"{title}:Polarity by Episode")
        plt.xlim(left=0)
        plt.legend()
        plt.gca().xaxis.get_major_locator().set_params(integer=True)

        plt.savefig(os.path.join(base_dir, "graph.png"))

    print("Graph saved!")

if __name__ == "__main__":
    graph("seasons-of-lovesome")