<template>
  <div style="border: 1px solid #ccc">
    <Toolbar
      ref="toolbarRef"
      style="border-bottom: 1px solid #ccc"
      :editor="editorRef"
      :defaultConfig="toolbarConfig"
    />
    <Editor
      :style="{ flex: 1, height: editorHeight + 'px', overflow: 'hidden' }"
      v-model="valueHtml"
      mode="simple"
      :defaultConfig="editorConfig"
      @onCreated="handleCreated"
    />
  </div>
</template>

<script setup>
import "@wangeditor/editor/dist/css/style.css"; // 引入 css
import "../qwebchannel.js";

import { onBeforeUnmount, onMounted, ref, shallowRef } from "vue";
import { Editor, Toolbar } from "@wangeditor/editor-for-vue";

const toolbarRef = shallowRef();
const editorRef = shallowRef();
const valueHtml = ref("");
const editorReady = ref(false)
const toolbarConfig = {};
const editorConfig = {};

const MIN_HEIGHT = 300;
const editorHeight = ref(MIN_HEIGHT);

toolbarConfig.toolbarKeys = [
  // 菜单 key
  "bold",
  "underline",
  "through",
  "italic",
  "color",
  "bgColor",
  "fontSize",
  "fontFamily",
  "|",
  "justifyLeft",
  "justifyCenter",
  "justifyRight",
  "lineHeight",
  "|",
  "clearStyle",
];

function updateEditorHeight() {
  const toolbarEl = toolbarRef.value?.$el || toolbarRef.value; // Vue 组件取 $el
  const toolbarHeight = toolbarEl ? toolbarEl.offsetHeight : 0;
  const newHeight = window.innerHeight - toolbarHeight - 20;
  editorHeight.value = Math.max(newHeight, MIN_HEIGHT);
}

onMounted(() => {
  document.title = "wangEditor";
  window.addEventListener('load', ()=>{
    updateEditorHeight();
    editorReady.value = true;
  });
  window.addEventListener("resize", updateEditorHeight);
});

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value;
  editorReady.value = false;
  if (editor == null) return;
  editor.destroy();
});

const handleCreated = (editor) => {
  editorRef.value = editor;

  window.getContent = () => {
    return editor.getHtml();
  };

  window.setContent = (html) => {
    editor.setHtml(html);
  };

  window.getWangEditorStatus = () => {
    return editorReady.value;
  };

  // 连接 Qt WebChannel
  if (!window.pyBridge) {
    new QWebChannel(qt.webChannelTransport, function (channel) {
      window.pyBridge = channel.objects.pyBridge;
    });
  }
};
</script>
