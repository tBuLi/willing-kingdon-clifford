import anywidget
import traitlets
from kingdon.graph import GraphWidget, walker, encode


class FragmentWidget(anywidget.AnyWidget):
    """
    This widget reads the fragment from the URL such that we can change animations when Reveal fragments are triggered.
    Currently just looks at the URL, maybe we can do better in the future.
    """
    _esm = """
    function render({ model, el }) {
      let state = () => model.get("state");
      let fragment = () => model.get("fragment");

      document.addEventListener("slidechanged", (x) => {
        model.set("state", [x.indexh, x.indexv]);
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
    state = traitlets.List([0, 0]).tag(sync=True)
    fragment = traitlets.Int(-1).tag(sync=True)
    slide = traitlets.Int(0)
    subslide = traitlets.Int(0)
    
    @traitlets.observe("slide", "subslide")
    def _pack_state(self, change):
        self.state = [self.slide, self.subslide]


class RevealWidget(GraphWidget):
    fragment_widget = traitlets.Instance(FragmentWidget, args=tuple(), kwargs=dict())
    graph_funcs = traitlets.Dict({})

    def __init__(self, *args, raw_subjects, **kwargs):
        kwargs['graph_funcs'] = raw_subjects[0]
        super().__init__(*args, raw_subjects=[raw_subjects[0].get((0, 0), lambda: [])], **kwargs)
        self.set_notifiers()

    @traitlets.default('draggable_points')
    def get_draggable_points(self):
        return []

    @traitlets.default('draggable_points_idxs')
    def get_draggable_points_idxs(self):
        return []
        
    def set_notifiers(self):
        self.fragment_widget.observe(self.changed_state, ['state', 'fragment'])
        
    def changed_state(self, change):
        slide_state = tuple(change['owner'].state)
        if slide_state in self.graph_funcs:
            raw_subjects = [self.graph_funcs[slide_state]]
            pre_subjects = self.graph_funcs[slide_state]()
            subjects = walker(encode(pre_subjects, root=True))

            # Update all variables at the same time to keep them in sync.
            self.raw_subjects, self.pre_subjects, self.subjects = [
                raw_subjects, pre_subjects, subjects
            ]
