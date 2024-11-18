<template>
    <div class="app-header">
      <template v-if="isLoading"> Loading... </template>
  
      <template v-else>
        <span v-if="showAllPages"> {{ pageCount }} page(s) </span>
  
        <span v-else>
          <button :disabled="page <= 1" @click="handlePreviousPage">❮</button>
          {{ page }} / {{ pageCount }}
          <button :disabled="page >= pageCount" @click="handleNextPage">❯</button>
        </span>

      </template>
    </div>
  
    <div class="app-content">
      <vue-pdf-embed
        ref="pdfRef"
        :source="pdfSource"
        :page="page"
        @rendered="handleDocumentRender"
        height="800"
      />
      <vue-pdf-embed
        ref="secondpdfRef"
        :source="pdfSource"
        :page="secondPage"
        @rendered="handleDocumentRender"
        height="800"
      />
    </div>
  </template>
  
<script setup>
  import { ref, onMounted, watch } from 'vue';
  import VuePdfEmbed from 'vue-pdf-embed';
  
  const isLoading = ref(true);
  const page = ref(null);
  const secondPage = ref(null);
  const pageCount = ref(1);
  const pdfSource = 'https://corsproxy.io/?https://kvongcmehsanalibrary.wordpress.com/wp-content/uploads/2021/07/harrypotter.pdf';
  const showAllPages = ref(false);
  const pdfRef = ref(null);
  
const handleNextPage = () => {
  page.value = page.value + 2;
  secondPage.value = secondPage.value + 2;
}
const handlePreviousPage = () => {
  page.value = page.value - 2;
  secondPage.value = secondPage.value - 2;
}
function handleDocumentRender(args) {
  console.log(args);
  isLoading.value = false;
  pageCount.value = pdfRef.value.pageCount;
}
watch(showAllPages, () => {
  page.value = showAllPages.value ? null : 1;
});
  
onMounted(() => {
  page.value = 1;
  secondPage.value = page.value + 1;
});
</script>

<style scoped>
.app-content{
  width: 80%;
  height: 80%;
  display: flex;
  flex-direction: row;
}
</style>
  