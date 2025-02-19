import React from 'react';
import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';

// Layouts
import MainLayout from './layouts/MainLayout';

// Pages
import Home from './pages/Home';
import NotFound from './pages/NotFound';

const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path='' element={<MainLayout />}>
        <Route index element={<Home />} />
        <Route path='*' element={<NotFound />} />
      </Route>
    )
  );

  return (
    <RouterProvider router={router} />
  );
};

export default App;