import React from "react";

const About = () => {
  return (
    <div className="min-h-[85vh] flex flex-col items-center py-10 px-4 md:px-8 lg:px-16">
      <h1 className="text-4xl font-bold mb-8">About Cryptoplace</h1>

      <div className="max-w-4xl w-full space-y-8">
        <section className="space-y-4">
          <h2 className="text-2xl font-semibold text-blue-500">Our Mission</h2>
          <p className="text-lg">
            At Cryptoplace, we're dedicated to providing real-time, accurate
            cryptocurrency data to empower investors and enthusiasts in making
            informed decisions. Our platform combines comprehensive market
            analysis with user-friendly interfaces to deliver the best crypto
            tracking experience.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-2xl font-semibold text-blue-500">
            What We Offer
          </h2>
          <ul className="list-disc list-inside space-y-2 text-lg">
            <li>Real-time cryptocurrency price tracking</li>
            <li>Multi-currency support (USD, INR, EUR)</li>
            <li>Detailed market analysis and charts</li>
            <li>User-friendly interface for all experience levels</li>
            <li>Comprehensive cryptocurrency information</li>
          </ul>
        </section>

        <section className="space-y-4">
          <h2 className="text-2xl font-semibold text-blue-500">
            Why Choose Us
          </h2>
          <p className="text-lg">
            Our platform stands out through its commitment to accuracy, ease of
            use, and comprehensive market coverage. Whether you're a seasoned
            investor or just starting your crypto journey, Cryptoplace provides
            the tools and information you need to navigate the cryptocurrency
            market effectively.
          </p>
        </section>
      </div>
    </div>
  );
};

export default About;
