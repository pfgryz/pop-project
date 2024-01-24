from typing import List
import matplotlib.pyplot as plt


def parse(pathname: str):
    data = []
    stats = []

    with open(pathname, "r") as handle:
        experiment = False
        statistics = False

        for line in handle:
            line = line.strip()

            if line == "BEGIN_EXPERIMENT":
                experiment = True
                continue
            elif line == "END_EXPERIMENT":
                experiment = False
                continue
            elif line == "BEGIN_STATISTICS":
                statistics = True
                continue
            elif line == "END_STATISTICS":
                statistics = False
                continue

            if experiment:
                elements = line.split(" ")

                iteration, max_iterations = elements[0].split("/")
                iteration = int(iteration)
                max_iterations = int(max_iterations)

                best = float(elements[1])
                best_total = float(elements[2])
                evaluations = int(elements[4])

                data.append(
                    (iteration, max_iterations, best, best_total, evaluations)
                )

            if statistics:
                stats.append(float(line))

    return data, stats


def generate_convergence_curve(logs: List[str], labels: List[str],
                               output: str):
    for log in logs:
        data, stats = parse(log)

        plt.plot(
            [d[4] for d in data],
            [d[3] for d in data],
            "-"
        )

    plt.title("Convergence curve")
    plt.ylabel("q(x)")
    plt.xlabel("Evaluations")
    plt.legend(labels)
    plt.savefig(output)
    plt.show()


def generate_ecdf(logs: List[str], labels: List[str], barriers, output: str):
    def crossed(x):
        return len([barrier for barrier in barriers if x < barrier]) / len(
            barriers)

    for log in logs:
        data, stats = parse(log)

        plt.plot(
            [d[4] for d in data],
            [crossed(d[3]) for d in data],
            "-"
        )

    plt.title("ECDF")
    plt.ylabel("relative number of barriers crossed")
    plt.xlabel("Evaluations")
    plt.legend(labels)
    plt.savefig(output)
    plt.show()


if __name__ == "__main__":
    generate_convergence_curve(
        ["mc1.log", "mc3.log", "mc5.log", "mc7.log"],
        ["Mc = 1", "Mc = 3", "Mc = 5", "Mc = 7"],
        "images/mc_conv.png")
    generate_ecdf(["mc1.log", "mc3.log", "mc5.log", "mc7.log"],
                  ["Mc = 1", "Mc = 3", "Mc = 5", "Mc = 7"],
                  list(range(int(50e7), int(250e7), int(2.5e7))),
                  "images/mc_ecdf.png")

    generate_convergence_curve(
        ["mp01.log", "mp03.log", "mp05.log", "mp07.log", "mp09.log"],
        ["Mp = 0.1", "Mp = 0.3", "Mp = 0.5", "Mp = 0.7", "Mp = 0.9"],
        "images/mp_conv.png"
    )
    generate_ecdf(
        ["mp01.log", "mp03.log", "mp05.log", "mp07.log", "mp09.log"],
        ["Mp = 0.1", "Mp = 0.3", "Mp = 0.5", "Mp = 0.7", "Mp = 0.9"],
        list(range(int(50e7), int(250e7), int(2.5e7))),
        "images/mp_ecdf.png"
    )

    generate_convergence_curve(
        ["ls.log", "lu.log", "lg.log", "rs.log", "ru.log", "rg.log"],
        ["Last + Single", "Last + Uniform",
            "Last + Gauss", "Random + Single",
            "Random + Uniform", "Random + Gauss"],
        "images/final_conv.png"
    )
    generate_ecdf(
        ["ls.log", "lu.log", "lg.log", "rs.log", "ru.log", "rg.log"],
        ["Last + Single", "Last + Uniform",
         "Last + Gauss", "Random + Single",
         "Random + Uniform", "Random + Gauss"],
        list(range(int(50e8), int(100e8), int(1e8))),
        "images/final_ecdf.png"
    )
    # generate_converg
