import DOMPurify from "dompurify";
import React from "react";
import { Link, RouteComponentProps } from "react-router-dom";
import Review from "../interfaces/Review";

interface State {
  searchTerm: string;
  reviews: Review[];
  previous: string;
  next: string;
  status: string;
}

export class ReviewList extends React.PureComponent<
  RouteComponentProps<any>,
  State
> {
  constructor(props: RouteComponentProps<any>) {
    super(props);
    const params = new URLSearchParams(this.props.location.search);
    this.state = {
      searchTerm: params.get("query") || "",
      reviews: [],
      previous: "",
      next: "",
      status: "",
    };
  }

  public async componentDidMount() {
    this.getReviews(`?query=${this.state.searchTerm}`);
  }

  private async getReviews(query: string) {
    this.setState({
      status: "Loading...",
    });
    const response = await fetch(`/api/reviews/${query}`);
    if (response.status !== 200) {
      return this.setState({ status: "Something went wrong." });
    }
    const data = await response.json();
    this.setState({
      reviews: data["results"],
      previous: data["previous"],
      next: data["next"],
      status: data["results"].length ? "" : "No reviews found.",
    });
  }

  private handleSearchTermChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    this.setState({
      searchTerm: event.target.value,
    });
  };

  private handlePreviousCLick = () => {
    const { previous } = this.state;
    if (previous) this.getReviews(new URL(previous).search);
  };

  private handleNextCLick = () => {
    const { next } = this.state;
    if (next) this.getReviews(new URL(next).search);
  };

  public render() {
    const { reviews, searchTerm, previous, next, status } = this.state;
    return (
      <div>
        <form style={{ margin: "2em" }}>
          <input
            name="query"
            placeholder="search..."
            value={searchTerm}
            onChange={this.handleSearchTermChange}
          />
          <button type="submit">Search</button>
        </form>
        {status ? (
          <div>{status}</div>
        ) : (
          <div
            style={{ textAlign: "left", marginLeft: "4em", marginRight: "4em" }}
          >
            {reviews.map((review: Review) => (
              <div>
                <h4>Review {review.id}</h4>
                <Link to={`/reviews/${review.id}`}>
                  <p
                    style={{ marginBottom: "4em" }}
                    dangerouslySetInnerHTML={{
                      __html: DOMPurify.sanitize(review.content, {
                        ALLOWED_TAGS: ["keyword"],
                      }),
                    }}
                  />
                </Link>
              </div>
            ))}
          </div>
        )}
        {previous ? (
          <button
            name="prev"
            style={{ margin: "1em" }}
            onClick={this.handlePreviousCLick}
          >
            Previous
          </button>
        ) : null}
        {next ? (
          <button
            name="prev"
            style={{ margin: "1em" }}
            onClick={this.handleNextCLick}
          >
            Next
          </button>
        ) : null}
      </div>
    );
  }
}
