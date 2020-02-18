const getUrl = (URL: string, projectId: any) => {
  return URL.replace('<projectId>', projectId);
};

export { getUrl };
