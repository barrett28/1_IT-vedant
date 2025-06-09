import React, { useState } from "react";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you can add your form submission logic
    console.log("Form submitted:", formData);
    alert("Thank you for your message! We will get back to you soon.");
    setFormData({ name: "", email: "", message: "" });
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="min-h-[85vh] flex flex-col items-center py-10 px-4 md:px-8 lg:px-16">
      <h1 className="text-4xl font-bold mb-8">Contact Us</h1>

      <div className="max-w-2xl w-full space-y-8">
        <p className="text-lg text-center">
          Have questions or suggestions? We'd love to hear from you. Send us a
          message and we'll respond as soon as possible.
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label htmlFor="name" className="block text-lg mb-2">
              Name
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="w-full p-3 rounded-lg bg-transparent border border-zinc-400 focus:border-blue-500 focus:outline-none"
            />
          </div>

          <div>
            <label htmlFor="email" className="block text-lg mb-2">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="w-full p-3 rounded-lg bg-transparent border border-zinc-400 focus:border-blue-500 focus:outline-none"
            />
          </div>

          <div>
            <label htmlFor="message" className="block text-lg mb-2">
              Message
            </label>
            <textarea
              id="message"
              name="message"
              value={formData.message}
              onChange={handleChange}
              required
              rows="5"
              className="w-full p-3 rounded-lg bg-transparent border border-zinc-400 focus:border-blue-500 focus:outline-none"
            ></textarea>
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-3 px-6 rounded-lg hover:bg-blue-600 transition-colors"
          >
            Send Message
          </button>
        </form>

        <div className="text-center space-y-4">
          <h2 className="text-2xl font-semibold text-blue-500">
            Other Ways to Reach Us
          </h2>
          <p className="text-lg">Email: support@cryptotracker.com</p>
          <p className="text-lg">Follow us on Twitter: @cryptotracker</p>
        </div>
      </div>
    </div>
  );
};

export default Contact;
