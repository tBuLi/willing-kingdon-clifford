import anywidget
import traitlets

class FragmentWidget(anywidget.AnyWidget):
    """
    This widget reads the fragment from the URL such that we can change animations when Reveal fragments are triggered.
    Currently just looks at the URL, maybe we can do better in the future.
    """
    _esm = """
    function render({ model, el }) {
      let state = () => model.get("state");
      let fragment = () => model.get("fragment");
      
      let btn = document.createElement("button");
      btn.innerHTML = `${state()}, ${fragment()}`;

      document.addEventListener("slidechanged", (x) => {
          console.log(x);
        model.set("state", (x.indexh, x.indexv));
        model.set("fragment", -1);
        model.save_changes();
        console.log(`${state()}, ${fragment()}`);
      });
      document.addEventListener("fragmentshown", (x) => {
        model.set("fragment", fragment() + 1);
        model.save_changes();
        console.log(`${state()}, ${fragment()}`);
      });
      document.addEventListener("fragmenthidden", (x) => {
        model.set("fragment", fragment() - 1);
        model.save_changes();
        console.log(`${state()}, ${fragment()}`);
      });
    }
    export default { render };
    """
    state = traitlets.Tuple((0, 0)).tag(sync=True)
    fragment = traitlets.Int(-1).tag(sync=True)
    slide = traitlets.Int(0)
    subslide = traitlets.Int(0)
    
    @traitlets.observe("slide", "subslide")
    def _pack_state(self, change):
        self.state = (self.slide, self.subslide)

# import anywidget
# import traitlets

# class FragmentWidget(anywidget.AnyWidget):
#     """
#     This widget reads the fragment from the URL such that we can change animations when Reveal fragments are triggered.
#     Currently just looks at the URL, maybe we can do better in the future.
#     """
#     _esm = """
#     function render({ model, el }) {
#       let slide = () => model.get("slide");
#       let subslide = () => model.get("subslide");
#       let fragment = () => model.get("fragment");
      
#       let btn = document.createElement("button");
#       btn.innerHTML = `${slide()} ${subslide()}, ${fragment()}`;

#       document.addEventListener("slidechanged", (x) => {
#         model.set("slide", x.indexh);
#         model.set("subslide", x.indexv);
#         model.set("fragment", -1);
#         model.save_changes();
#         console.log(`${slide()} ${subslide()}, ${fragment()}`);
#       });
#       document.addEventListener("fragmentshown", (x) => {
#         model.set("fragment", fragment() + 1);
#         model.save_changes();
#         console.log(`${slide()} ${subslide()}, ${fragment()}`);
#       });
#       document.addEventListener("fragmenthidden", (x) => {
#         model.set("fragment", fragment() - 1);
#         model.save_changes();
#         console.log(`${slide()} ${subslide()}, ${fragment()}`);
#       });
#     }
#     export default { render };
#     """
#     slide = traitlets.Int(0).tag(sync=True)
#     subslide = traitlets.Int(0).tag(sync=True)
    
#     fragment = traitlets.Int(-1).tag(sync=True)

#     @property
#     def state(self):
#         return self.slide, self.subslide, self.fragment

#     @property
#     def slide_state(self):
#         return self.slide, self.subslide

 