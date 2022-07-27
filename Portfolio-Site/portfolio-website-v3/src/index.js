import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import ContactForm from './Components/contactForm.js';
import FooterArea from './Components/footer';
import NavBar from './Components/navBar';
import PersonalSpecs from './Components/personalSpecs';
//import LoginPage from './Components/loginPage';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <NavBar />
    <PersonalSpecs />
    <ContactForm />
    <FooterArea />
  </React.StrictMode>
);


