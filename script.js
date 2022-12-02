gsap.config({ trialWarn: false });
console.clear();
gsap.registerPlugin(ScrollTrigger, SplitText);
let split = new SplitText("h1", { type: "lines" });

function makeItHappen() {
  split.lines.forEach((target) => {
    gsap.to(target, {
      backgroundPositionX: 0,
      ease: "none",
      scrollTrigger: {
        trigger: target,
        markers: false,
        scrub: 0.5,
        start: "top center",
        end: "bottom center",
      },
    });
  });
}

let someDelay = gsap.delayedCall(0.2, newTriggers).pause();
window.addEventListener("resize", () => someDelay.restart(true));

function newTriggers() {
  ScrollTrigger.getAll().forEach((trigger) => {
    trigger.kill();
  });
  split.split();
  makeItHappen();
}

makeItHappen();
