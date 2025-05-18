import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import NewCalibration from './pages/NewCalibration';
import Results from './pages/Results';
import QueryResults from './pages/QueryResults';
import Login from './pages/Login';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Dashboard} />
        <Route path="/new" component={NewCalibration} />
        <Route path="/results/:id" component={Results} />
        <Route path="/search" component={QueryResults} />
        <Route path="/login" component={Login} />
      </Switch>
    </Router>
  );
}

export default App;