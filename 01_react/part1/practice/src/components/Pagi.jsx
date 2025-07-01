import React, { useEffect, useState } from "react";

const PaginatedPosts = () => {
  const [posts, setPosts] = useState([]);
  const [page, setPage] = useState(1); // Current page
  const [loading, setLoading] = useState(false);

  const postsPerPage = 10;

  useEffect(() => {
    const fetchPosts = async () => {
      setLoading(true);
      const res = await fetch(
        `https://jsonplaceholder.typicode.com/posts?_limit=${postsPerPage}&_page=${page}`
      );
      const data = await res.json();
      setPosts(data);
      setLoading(false);
    };

    fetchPosts();
  }, [page]);

  const handlePrev = () => {
    if (page > 1) setPage((prev) => prev - 1);
  };

  const handleNext = () => {
    if (page < 10) setPage((prev) => prev + 1); // 100 posts / 10 per page
  };

  return (
    <div>
      <h2>Paginated Posts (Page {page})</h2>

      {loading ? (
        <p>Loading...</p>
      ) : (
        posts.map((post) => (
          <div key={post.id}>
            <h4>{post.title}</h4>
            {/* <p>{post.body}</p> */}
            <hr />
          </div>
        ))
      )}

      <div style={{ marginTop: "20px" }}>
        <button onClick={handlePrev} disabled={page === 1}>
          ⬅ Previous
        </button>
        <button onClick={handleNext} disabled={page === 10}>
          Next ➡
        </button>
      </div>
    </div>
  );
};

export default PaginatedPosts;
