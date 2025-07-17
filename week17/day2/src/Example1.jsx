import React, { Component } from 'react';
import data from './data.json';

class Example1 extends Component {
  render() {
    return (
      <div>
        <ul>
          {data.SocialMedias.map((item, index) => (
            <li key={index}>
              <strong>{item.platform}</strong> <a href={item.url}>{item.url}</a>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default Example1;
