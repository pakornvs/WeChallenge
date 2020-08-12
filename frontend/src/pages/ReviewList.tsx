import DOMPurify from "dompurify";
import React from "react";
import { Link, RouteComponentProps } from "react-router-dom";
import Review from "../interfaces/Review";

interface State {
  reviews: Review[];
  searchTerm: string;
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
      reviews: [],
      searchTerm: params.get("query") || "",
      status: "",
    };
  }

  public async componentDidMount() {
    this.getReviews();
  }

  private async getReviews() {
    this.setState({
      status: "Loading...",
    });
    const response = await fetch(
      `/api/reviews/?query=${this.state.searchTerm}`
    );
    if (response.status !== 200) {
      return this.setState({ status: "Something went wrong." });
    }
    const data = await response.json();
    const reviews = data["results"];
    this.setState({
      reviews: reviews,
      status: reviews.length ? "" : "No reviews found.",
    });
  }

  private handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({
      searchTerm: event.target.value,
    });
  };

  public render() {
    const { reviews, searchTerm, status } = this.state;
    return (
      <div>
        <form style={{ margin: "1em" }}>
          <input
            name="query"
            placeholder="search..."
            value={searchTerm}
            onChange={this.handleChange}
          />
          <button type="submit">Search</button>
        </form>
        {status ? (
          <div>{status}</div>
        ) : (
          <ul style={{ listStyleType: "decimal", textAlign: "left" }}>
            {reviews.map((review: Review) => (
              <Link key={review.id} to={`/reviews/${review.id}`}>
                <li
                  style={{ margin: "1em" }}
                  dangerouslySetInnerHTML={{
                    __html: DOMPurify.sanitize(review.content, {
                      ALLOWED_TAGS: ["keyword"],
                    }),
                  }}
                />
              </Link>
            ))}
          </ul>
        )}
      </div>
    );
  }
}
