import './navBar.css';

function navBar() {
    return (
      <header>
        <div className="navBarContainer">
          <div className="namelogo"><span className="nameSpan">Wayne Thomson</span> Portfolio</div>
            <nav>
              <ul className="pageLinks">
                <li><a href="#">Home</a></li>
                <li><a href="#">Projects</a></li>
                <li><a href="#">Blog</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href='#'>Login</a></li>
              </ul>
              <ul className='socialCrap'>
                <li><a href="#">LN</a></li>
                <li><a href="#">CA</a></li>
                <li><a href="#">D</a></li>
              </ul>
            </nav>
        </div>
      </header>
    );
  }
  
  export default navBar;