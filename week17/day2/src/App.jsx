import React from 'react';
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav, Container } from 'react-bootstrap';

import ErrorBoundary from './ErrorBoundary';
import HomeScreen from './HomeScreen';
import ProfileScreen from './ProfileScreen';
import ShopScreen from './ShopScreen';
import PostList from './PostList';
import Example1 from './Example1';
import Example2 from './Example2';
import Example3 from './Example3';
import Exercise4 from './Exercise4';

function App() {
  return (
    <BrowserRouter>
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand>XP Exercises</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link as={NavLink} to="/">Home</Nav.Link>
            <Nav.Link as={NavLink} to="/profile">Profile</Nav.Link>
            <Nav.Link as={NavLink} to="/shop">Shop</Nav.Link>
            <Nav.Link as={NavLink} to="/posts">Posts</Nav.Link>
            <Nav.Link as={NavLink} to="/example1">Example1</Nav.Link>
            <Nav.Link as={NavLink} to="/example2">Example2</Nav.Link>
            <Nav.Link as={NavLink} to="/example3">Example3</Nav.Link>
            <Nav.Link as={NavLink} to="/exercise4">Exercise4</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <Container className="mt-3">
        <Routes>
          <Route path="/" element={
            <ErrorBoundary><HomeScreen /></ErrorBoundary>
          } />
          <Route path="/profile" element={
            <ErrorBoundary><ProfileScreen /></ErrorBoundary>
          } />
          <Route path="/shop" element={
            <ErrorBoundary><ShopScreen /></ErrorBoundary>
          } />
          <Route path="/posts" element={<PostList />} />
          <Route path="/example1" element={<Example1 />} />
          <Route path="/example2" element={<Example2 />} />
          <Route path="/example3" element={<Example3 />} />
          <Route path="/exercise4" element={<Exercise4 />} />
        </Routes>
      </Container>
    </BrowserRouter>
  );
}

export default App;
