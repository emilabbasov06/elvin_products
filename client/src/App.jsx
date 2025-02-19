import React from 'react';
import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';

// Layouts
import MainLayout from './layouts/MainLayout';

// Pages
import Home from './pages/Home';
import Elektrik from './pages/Elektrik';
import Santexnika from './pages/Santexnika';
import Istilik from './pages/Istilik';
import Xirdavat from './pages/Xirdavat';
import NotFound from './pages/NotFound';

const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path='' element={<MainLayout />}>
        <Route index element={<Home />} />
        <Route path='/elektrik' element={<Elektrik />} />
        <Route path='/santexnika' element={<Santexnika />} />
        <Route path='/istilik' element={<Istilik />} />
        <Route path='/xirdavat' element={<Xirdavat />} />
        <Route path='*' element={<NotFound />} />
      </Route>
    )
  );

  return (
    <RouterProvider router={router} />
  );
};

export default App;