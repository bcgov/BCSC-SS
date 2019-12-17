FROM centos/s2i-core-centos7


# PostgreSQL image for OpenShift.
# Volumes:
#  * /var/lib/psql/data   - Database cluster for PostgreSQL
# Environment:
#  * $POSTGRESQL_USER     - Database user name
#  * $POSTGRESQL_PASSWORD - User's password
#  * $POSTGRESQL_DATABASE - Name of the database to create
#  * $POSTGRESQL_ADMIN_PASSWORD (Optional) - Password for the 'postgres'
#                           PostgreSQL administrative account
# @see https://github.com/sclorg/postgresql-container/blob/generated/10/Dockerfile.rhel8

ENV POSTGRESQL_VERSION=11 \
    HOME=/var/lib/pgsql \
    PGUSER=postgres \
    APP_DATA=/opt/app-root

ENV SUMMARY="PostgreSQL is an advanced Object-Relational database management system" \
    DESCRIPTION="PostgreSQL is an advanced Object-Relational database management system (DBMS). \
The image contains the client and server programs that you'll need to \
create, run, maintain and access a PostgreSQL DBMS server."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="PostgreSQL 11" \
      io.openshift.expose-services="5432:postgresql" \
      io.openshift.tags="database,postgresql,postgresql11,postgresql-11" \
      io.openshift.s2i.assemble-user="26" \
      name="rhel8/postgresql-11" \
      com.redhat.component="postgresql-11-container" \
      version="1" \
      usage="podman run -d --name postgresql_database -e POSTGRESQL_USER=user -e POSTGRESQL_PASSWORD=pass -e POSTGRESQL_DATABASE=db -p 5432:5432 rhel8/postgresql-10" \
      maintainer="Alec Wenzowski <alec@button.is>"

EXPOSE 5432

COPY root/usr/libexec/fix-permissions /usr/libexec/fix-permissions

# TODO: Rename the builder environment variable to inform users about application you provide them
# ENV BUILDER_VERSION 1.0

# TODO: Set labels used in OpenShift to describe the builder image
#LABEL io.k8s.description="Platform for building xyz" \
#      io.k8s.display-name="builder x.y.z" \
#      io.openshift.expose-services="8080:http" \
#      io.openshift.tags="builder,x.y.z,etc."

# TODO: Install required packages here:
# yum install -y yum-utils
# yum repolist all
# repoquery --list readline
ENV PATH /opt/app-root/src/bin:/opt/app-root/bin:/usr/local/pgsql/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

COPY dnf.conf .

RUN yum install epel-release -y && \
    yum install dnf -y

RUN INSTALL_PKGS="nss_wrapper make gcc vim-common kernel-headers zlib-devel libcurl-devel git perl patch autoconf automake libxml2-devel" && \
    dnf install -y --setopt=tsflags=nodocs --config=dnf.conf $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    dnf clean all -y

RUN curl https://ftp.postgresql.org/pub/source/v11.4/postgresql-11.4.tar.gz | tar xz && \
    pushd postgresql-11.4 && \
    ./configure --without-readline --with-libxml && \
    make && \
    make install && \
    popd && \
    rm -r postgresql-11.4 && \
    localedef -f UTF-8 -i en_US en_US.UTF-8 && \
    groupadd -g 26 postgres && \
    adduser -u 26 -g 26 postgres && \
    test "$(id postgres)" = "uid=26(postgres) gid=26(postgres) groups=26(postgres)" && \
    mkdir -p /var/lib/pgsql/data && \
    mkdir -p /var/run/postgresql && \
    /usr/libexec/fix-permissions /var/lib/pgsql /var/run/postgresql

RUN git clone -b 'v8.2.2' --single-branch  https://github.com/citusdata/citus.git && \
    pushd citus  && \
    ./configure && \
    make && \
    make install && \
    popd && \
    rm -r citus

# TODO: pg needs to be running to check TAP install
# make installcheck && \
RUN git clone -b 'v1.0.0' --single-branch https://github.com/theory/pgtap.git && \
    pushd pgtap  && \
    make && \
    make install && \
    popd && \
    rm -r pgtap

# Get prefix path and path to scripts rather than hard-code them in scripts
ENV CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts/postgresql \
    ENABLED_COLLECTIONS=

COPY root /
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Not using VOLUME statement since it's not working in OpenShift Online:
# https://github.com/sclorg/httpd-container/issues/30
# VOLUME ["/var/lib/pgsql/data"]

# S2I permission fixes
# --------------------
# 1. unless specified otherwise (or - equivalently - we are in OpenShift), s2i
#    build process would be executed as 'uid=26(postgres) gid=26(postgres)'.
#    Such process wouldn't be able to execute the default 'assemble' script
#    correctly (it transitively executes 'fix-permissions' script).  So let's
#    add the 'postgres' user into 'root' group here
#
# 2. we call fix-permissions on $APP_DATA here directly (UID=0 during build
#    anyways) to assure that s2i process is actually able to _read_ the
#    user-specified scripting.
RUN usermod -a -G root postgres && \
    /usr/libexec/fix-permissions --read-only "$APP_DATA"

USER 26

ENTRYPOINT ["container-entrypoint"]
CMD ["run-postgresql"]