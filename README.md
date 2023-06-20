
# Movie Recommendation System

This project implements a movie recommendation system based on content-based filtering using cosine similarity. It recommends movies that are similar to a user-specified movie.

## Prerequisites

To run this code, you need to have the following dependencies installed:

- Python 3.x
- pandas
- numpy
- scikit-learn

## Dataset

The movie dataset used in this project is stored in a CSV file named `movie_dataset.csv`. It contains information about movies such as title, keywords, cast, genres, and director.

## Usage

1. Ensure that the `movie_dataset.csv` file is located in the same directory as the Python script.

2. Run the Python script `movie_recommendation.py`.

3. Enter the name of a movie when prompted. The system will provide the top 3 similar movies based on the content of the entered movie.

## Implementation

The code performs the following steps:

1. Imports the necessary libraries, including pandas, numpy, CountVectorizer, and cosine_similarity.

2. Loads the movie dataset from the `movie_dataset.csv` file into a pandas DataFrame.

3. Defines a function `combine_features` that concatenates the keywords, cast, genres, and director of each movie into a single string.

4. Fills any missing values in the DataFrame with empty strings.

5. Creates a new column called `combined_features`, which contains the combined features of each movie.

6. Uses CountVectorizer to convert the combined features into a matrix of token counts.

7. Computes the cosine similarity matrix using the count matrix.

8. Defines two helper functions: `get_title_from_index` and `get_index_from_title`, which retrieve the title or index of a movie based on its index or title, respectively.

9. Prompts the user to enter a movie.

10. Retrieves the index of the entered movie.

11. Computes the similarity scores between the entered movie and all other movies.

12. Sorts the similar movies based on their similarity scores in descending order.

13. Prints the top 3 similar movies to the entered movie.



## Acknowledgments

The code in this project is based on the concepts of content-based filtering and cosine similarity. It leverages the scikit-learn library for vectorization and similarity computation.

## References

- [Scikit-learn documentation](https://scikit-learn.org/)
- [Pandas documentation](https://pandas.pydata.org/)
- [NumPy documentation](https://numpy.org/)

Please update the file paths and modify the content as per your specific requirements.
