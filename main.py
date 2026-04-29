import geopandas as gpd
import matplotlib.pyplot as plt


DATA_URL = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"


def load_data(url: str) -> gpd.GeoDataFrame:
    """Load geospatial data from a public GeoJSON URL."""
    return gpd.read_file(url)


def plot_data(data: gpd.GeoDataFrame) -> None:
    """Plot the geospatial data on a simple map."""
    fig, ax = plt.subplots(figsize=(12, 8))
    data.plot(ax=ax, color="lightblue", edgecolor="black", linewidth=0.4)
    ax.set_title("World Countries from GeoJSON", fontsize=16)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()


def main() -> None:
    geodata = load_data(DATA_URL)
    print("First five rows of the dataset:")
    print(geodata.head())
    plot_data(geodata)


if __name__ == "__main__":
    main()
