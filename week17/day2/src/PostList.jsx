import React from 'react';
import posts from './posts.json';

function PostList() {
  return (
    <div>
      <h2>Hi This is a Title</h2>
      {posts.map(post => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
        </div>
      ))}
    </div>
  );
}

export default PostList;
