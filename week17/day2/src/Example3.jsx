import React, { Component } from "react";
import data from "./data.json";

class Example3 extends Component {
  render() {
    return (
      <div>
        {data.Experiences.map((exp, index) => (
          <div key={index} style={{ marginBottom: "40px" }}>
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
              alt="No image available"
              style={{
                display: "block",
                width: "150px",
                height: "150px",
                borderRadius: "50%",
                marginBottom: "10px",
              }}
            />

            <a href="#" style={{ display: "block", color: "purple" }}>
              {exp.company}
            </a>

            <br/>

            <p>
              <strong>{exp.role}</strong>
            </p>
            <p>
              {exp.years}
              {exp.location ? ` ${exp.location}` : ""}
            </p>
            <p>{exp.description}</p>
            <p>{exp.works}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default Example3;
