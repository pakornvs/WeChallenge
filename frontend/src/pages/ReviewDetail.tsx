import React from "react";
import { RouteComponentProps } from "react-router-dom";

export class ReviewDetail extends React.PureComponent<
  RouteComponentProps<{ id: string }>
> {
  public state = {
    id: 0,
    content: "",
    status: "Loading...",
  };

  public async componentDidMount() {
    const response = await fetch(`/api/reviews/${this.props.match.params.id}/`);
    if (response.status !== 200) {
      return this.setState({ status: "Something went wrong." });
    }
    const data = await response.json();
    this.setState({ id: data.id, content: data.content, status: "" });
  }

  private handleContentChange = (
    event: React.ChangeEvent<HTMLTextAreaElement>
  ) => {
    this.setState({
      content: event.target.value,
    });
  };

  private handleUpdateClick = async () => {
    this.setState({ status: "Loading..." });
    const requestOptions = {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: this.state.content }),
    };
    const response = await fetch(
      `/api/reviews/${this.props.match.params.id}/`,
      requestOptions
    );
    if (response.status !== 200) {
      return this.setState({ status: "Something went wrong." });
    }
    this.setState({ status: "" });
  };

  public render() {
    const { id, content, status } = this.state;
    if (status) return <div style={{ margin: "1em" }}>{status}</div>;
    return (
      <div>
        <h4>Review {id}</h4>
        <textarea
          style={{
            width: "50vw",
            height: "50vh",
          }}
          value={content}
          onChange={this.handleContentChange}
        />
        <button
          style={{
            display: "block",
            marginLeft: "auto",
            marginRight: "auto",
          }}
          onClick={this.handleUpdateClick}
        >
          Update
        </button>
      </div>
    );
  }
}
