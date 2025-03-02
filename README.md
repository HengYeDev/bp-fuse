# Fuse

Learn about circuits with ease

By Charlie K. (@crkalapat) and Heng Ye (@HengYeDev)

(Note: We originally planned to host the code on GitLab, but then realized that we had to use GitHub, which is why there is a late initial commit. We also used PyCharm instead of Git version control to primarily collaborate, due to small group size.)

## Inspiration

Normally, whenever you make a mistake with coding, there is no harm done. The software can re-run most of the time, and it will have a very minor maximum cost to re-run. However, with hardware, mistakes can be expensive. Mistakes can blow out components, and they can also cause the price of a project to go up. To address this problem, we created Fuse (based off the electrical component that saves circuits from melting). Fuse's goal is to serve as a helper for hardware projects, in order to prevent mistakes and give the user a better time overall.

## What it does

Fuse is a web application that uses different machine learning models to help the user with their circuits. We use a custom machine learning model that we trained to identify components on a breadboard, and then we feed that image to GPT-4o to provide textual analysis of the circuit to the user. Once the analysis is complete, the user can download the results of it for their own personal reference.

## How we built it

For the frontend, we used template code online as a foundation. From there, we tweaked it to best suit our needs, adding our own HTML, JS, CSS, multiple pages, and integration with our backend. For the backend, we used Flask, YOLOv8, OpenAI, JQuery, and Ajax.

## Challenges we ran into

For the backend, machine learning models appear easy to train, but it's hard to get them working on real-world data. We tried to train an ML model to identify LEDs, but we couldn't get a good enough dataset for the model to work well. Additionally, we had to train the resistor ML model more than once in order for it to function well.

## Accomplishments that we're proud of

We are proud of the fact that we trained our own ML model for this hackathon that is capable of robustly identifying resistors on a breadboard. Additionally, we are also proud of the UI and UX that we achieved on the webpage, and the integration that we did between many different code libaries (eg. OpenAI, our own ML model, Ajax, etc.)

## What we learned

Each member of the team learned something new and unique as a result of this hackathon. Charlie made his first multi-page web application with Fuse, and learned how to make a high-quality website front-end that has a good UI and UX. Heng learned how to train an ML model, and how to incorporate it along with all the other backend elements.

## What's next for our project

Fuse's goal is to help users learn about circuits that they built, and component identification is essential to this. If we had more time, we would train and create more ML models for other commonly used circuit components (like capacitors and LEDs), and the extra time would also allow us to optimize model performance and identification confidence values.

## Dependencies

`pip install -U ultralytics Pillow`