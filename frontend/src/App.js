import React from 'react';
import './App.css';
import { Route, Redirect, Switch } from 'react-router-dom'
import { Home, Navigation } from 'features/common/index';
import { History} from 'features/history'

function App() {
  return (<>
  {/* <Home/> */}
  <Navigation/>
  {/* <Test/> */}
  <Switch>
    <Route exact path='/' component= { Home }/>
    <Redirect from='/home' to= { '/' }/>
    <Route exact path='/history' component= { History }/>
  </Switch>
  </>);
}

export default App;
