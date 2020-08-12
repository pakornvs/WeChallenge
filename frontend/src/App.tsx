import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./App.css";
import { ReviewDetail } from "./pages/ReviewDetail";
import { ReviewList } from "./pages/ReviewList";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path={["/", "/reviews"]} component={ReviewList} />
          <Route exact path="/reviews/:id" component={ReviewDetail} />
          <Route
            path="/"
            render={() => <div style={{ margin: "1em" }}>404 Not Found</div>}
          />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
