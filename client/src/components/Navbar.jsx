import React, { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { Menu, X } from "lucide-react";

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => setMenuOpen(!menuOpen);
  const closeMenu = () => setMenuOpen(false);

  return (
    <header className="flex items-center justify-center p-5">
      <div className="w-[98%] flex items-center justify-between p-5 bg-white/50 backdrop-blur-lg shadow-lg border border-white/20 rounded-xl">
        <div className="text-3xl font-semibold">
          <NavLink className="text-red-400 bg-text" to="/" onClick={closeMenu}>LOGO</NavLink>
        </div>

        <button onClick={toggleMenu} className="md:hidden focus:outline-none">
          {menuOpen ? <X size={28} /> : <Menu size={28} />}
        </button>

        <nav
          className={`fixed top-0 left-0 h-fit w-64 shadow-lg transform ${menuOpen ? "translate-x-0 bg-white/90 rounded-xl" : "-translate-x-full"} transition-transform duration-300 md:static md:translate-x-0 md:w-auto md:bg-transparent md:shadow-none`}
        >
          <ul className="flex flex-col md:flex-row items-start md:items-center gap-4 text-md font-semibold p-5 md:p-0">
            <li><NavLink className="hover:text-red-400 duration-500" to="/" onClick={closeMenu}>Ana sehife</NavLink></li>
            <li><NavLink className="hover:text-red-400 duration-500" to="/elektrik" onClick={closeMenu}>Elektrik</NavLink></li>
            <li><NavLink className="hover:text-red-400 duration-500" to="/santexnika" onClick={closeMenu}>Santexnika</NavLink></li>
            <li><NavLink className="hover:text-red-400 duration-500" to="/istilik" onClick={closeMenu}>Istilik</NavLink></li>
            <li><NavLink className="hover:text-red-400 duration-500" to="/xirdavat" onClick={closeMenu}>Xirdavat</NavLink></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Navbar;
