import React from 'react';
import {BrowserRouter, Route, Link, NavLink, Switch} from 'react-router-dom';

export default function RouterTest() {
    
    const activeStyle = {
        color:"red"
    }
    
    return (
        <div>
            <BrowserRouter>
            <div id = 'menu'>
                <NavLink to="/" activeStyle={activeStyle}>Home</NavLink>
                <NavLink to="/students" activeStyle={activeStyle}>Student</NavLink>
            </div>

            <div id = "content">
                <Switch>
                    <Route exact path="/" component={Home}/>
                    <Route path="/students" component={Student}/>
                    <Route component={NoPage}/>
                </Switch>
            </div>
            </BrowserRouter>
        </div>
    )
}

function Home() {

    return(
        <div>
            HOME
        </div>
    )
}

function Student() {

    return(
        <div>
            STUDENTS
        </div>
    )
}

function NoPage() {

    return(
        <div>
            NoPage
        </div>
    )
}