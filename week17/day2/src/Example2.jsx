import React, { Component } from 'react';
import data from './data.json';

class Example2 extends Component {
  render() {
    const { languages, tools } = data.Skills;

    return (
      <div>
        <h4>Programming Language</h4>
        <ul>
          {languages.map((lang, index) => (
            <li key={index}>{lang}</li>
          ))}
        </ul>

        <h4>Web-Based Application Development</h4>
        <ul>
          {tools.map((tool, index) => (
            <li key={index}>{tool}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default Example2;
