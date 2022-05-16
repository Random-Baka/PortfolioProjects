import React from 'react'

import { Header, Stats, Details, Contact, Footer } from './containers';
import { Navbar } from "./components";
 
const Home = () => (
  <div>
    <h1>Test</h1>
    <Navbar />
    <Header />
    <Stats />
    <Details />
    <Contact />
    <Footer />
  </div>
)

export default Home